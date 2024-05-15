from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from scrapli import Scrapli
from scrapli.response import Response as ScrapliResponse

from app.config.device_config import path_config_parse, template
from app.config.driver import device, driver
from app.enums import commands, configurations
from app.logger import logger
from app.routers.api_schemas.configuration import (
    BatchDeviceConfigurationData,
    DeviceConfigurationData,
)
from app.routers.api_schemas.base import BaseAPIResponse, APIResponseStatusCode


async def _parse_config(config: ScrapliResponse):
    return config.ttp_parse_output(str(path_config_parse))[0]


def _settings_driver(hostname: str):
    device_settings = device._devices
    driver_settings = driver._settings

    if driver_settings.get("host") is None:
        host = device_settings.get(hostname)
        driver_settings.update({"host": host})
    return driver_settings


async def get_device_configuration(
    hostname: str,
    command: commands.ShowCommandCisco | None = None,
) -> DeviceConfigurationData:
    if not command:
        command = commands.ShowCommandCisco.ALL_CONFIG
    logger.info(f"Connect to device: {hostname}")
    with Scrapli(**_settings_driver(hostname)) as ssh:
        data = ssh.send_command(command)
        logger.info(f"Getting configurations with {hostname}")
        if data.failed:
            raise HTTPException(
                status_code=503,
                detail=f"Команда {command} не была успешно обработана на устройстве {data}.",
            )
        logger.info("The configuration has been successfully received")
        config = await _parse_config(config=data)

        return DeviceConfigurationData(**config).model_dump()


async def configure_device(
    hostname: str,
    params: DeviceConfigurationData,
    action: (
        configurations.ActionConfiguration | None
    ) = configurations.ActionConfiguration.create,
):
    configurations = params.configuration.model_dump(exclude_none=True)
    cmds = template.render(configurations, action=action).split("\n")
    cmds = dict.fromkeys(cmds)
    if "" in cmds:
        cmds = [cmd for cmd in cmds if cmd != '']
    logger.info(f"Commands for configure: {cmds}")
    logger.info(f"Connect to device: {hostname}")
    with Scrapli(**_settings_driver(hostname)) as ssh:
        logger.info(f"Device {hostname} configuring")
        res = ssh.send_configs(
            cmds,
        )
        if res.failed:
            raise HTTPException(
                status_code=APIResponseStatusCode.nok,
                detail=f"Во время конфигурации устройства произошла ошибка {res}",
            )
        logger.info(f"The device {hostname} has been successfully configured")
        return JSONResponse(status_code=APIResponseStatusCode.created, content=BaseAPIResponse.get(APIResponseStatusCode.created))


async def configure_devices(
    params: BatchDeviceConfigurationData,
    action: (
        configurations.ActionConfiguration | None
    ) = configurations.ActionConfiguration.create,
):
    for param in params.configurations:
        await configure_device(
            hostname=param.configuration.hostname, params=param, action=action
        )
