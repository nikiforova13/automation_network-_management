from scrapli import Scrapli

from config.driver import driver
import pathlib

from app.routers.api_schemas.configuration import DeviceConfigurationData

PATH_CONFIG_PARSE = (
    pathlib.Path(__file__)
    .absolute()
    .parent.parent.joinpath("templates_device")
    .joinpath("parse_config")
)


def _parse_config(s: str | None = None, info: str | None = None):
    path = PATH_CONFIG_PARSE.joinpath(s)
    b = info.ttp_parse_output(str(path))
    return b[0]


def get_device_configuration(s: str | None = None, command: str | None = None):
    with Scrapli(**driver._settings) as ssh:
        print(PATH_CONFIG_PARSE)
        a = ssh.send_command(command)
        return _parse_config(s, a)


def configure_device(params: DeviceConfigurationData):
    if a:= params.configuration.model_dump(exclude_none=True):
        print(params)
        print(a)
    for obj, data in a.items():
        print(obj)
        print(data)
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
