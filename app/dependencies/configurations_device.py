from scrapli import Scrapli

from config.driver import driver
from config.device_config import path_config_parse, template
from app.routers.api_schemas.configuration import DeviceConfigurationData


def _parse_config(info: str | None = None):
    b = info.ttp_parse_output(str(path_config_parse))
    print(b)
    return b[0]


def get_device_configuration(command: str | None = None):
    with Scrapli(**driver._settings) as ssh:
        a = ssh.send_command(command)
        return _parse_config(a)


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
