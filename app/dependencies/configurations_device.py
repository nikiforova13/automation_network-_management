import ipaddress
from scrapli import Scrapli

from config.driver import driver
from config.device_config import path_config_parse, template
from app.routers.api_schemas.configuration import DeviceConfigurationData
from app.enums import commands, configurations
from scrapli.response import Response as ScrapliResponse
from fastapi.exceptions import ResponseValidationError, HTTPException
from fastapi.responses import Response


async def _parse_config(config: ScrapliResponse):
    return config.ttp_parse_output(str(path_config_parse))[0]


async def get_device_configuration(
    command: commands.ShowCommandCisco | None = None,
) -> DeviceConfigurationData:
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


async def configure_device(
    params: DeviceConfigurationData,
    action: configurations.Action | None = configurations.Action.create,
):
    configurations = params.configuration.model_dump(exclude_none=True)
    cmds = template.render(configurations, action=action).split("\n")
    cmds.remove("")
    print(cmds)
    with Scrapli(**driver._settings) as ssh:
        res = ssh.send_configs(
            cmds,
        )

        if res.failed:
            raise HTTPException(
                status_code=503,
                detail=f"Во время конфигурации устройства произошла ошибка",
            )
        return Response(status_code=200, content="Successful Response")


def subnet_masks_with_prefix():
    subnet_masks = []
    for prefix_length in range(33):
        network = ipaddress.IPv4Network(("0.0.0.0", prefix_length), strict=False)
        subnet_masks.append(f"{str(network.netmask)} /{prefix_length}")
    return subnet_masks
