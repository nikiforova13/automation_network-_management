from scrapli import Scrapli

from config.driver import driver
from config.device_config import path_config_parse, template
from app.routers.api_schemas.configuration import DeviceConfigurationData
from app.enums import commands
from scrapli.response import Response
from fastapi.exceptions import ResponseValidationError, HTTPException


async def _parse_config(config: Response):
    return config.ttp_parse_output(str(path_config_parse))[0]


async def get_device_configuration(command: commands.ShowCommandCisco | None = None) -> DeviceConfigurationData:
    if not command:
        command = commands.ShowCommandCisco.ALL_CONFIG
    with Scrapli(**driver._settings) as ssh:
        data = ssh.send_command(command)
        if data.failed:
            # return ResponseValidationError(errors='Команда не была успешно обработана')
            raise HTTPException(
                status_code=503,
                detail=f"Команда {command} не была успешно обработана на устройстве",
            )
        return await _parse_config(config=data)


def configure_device(params: DeviceConfigurationData):
    configurations = params.configuration.model_dump(exclude_none=True)
    commands = template.render(configurations)
    print(commands)
    print(commands.split("\n"))

    with Scrapli(**driver._settings) as ssh:
        ...
        # a = ssh.send_configs(
        #     ["interface FastEthernet0/1", "ip address 10.10.9.9 255.255.255.0"],
        # )
        # a = ssh.send_configs(
        # )
        # print(a)
        # if a.failed:
        #     raise ValueError(a.result)
        # return a
