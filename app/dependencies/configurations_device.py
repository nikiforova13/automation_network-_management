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
PATH_CONFIG_CONFIGURE = (
    pathlib.Path(__file__)
    .absolute()
    .parent.parent.joinpath("templates_device")
    .joinpath("configure_config")
)
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader(PATH_CONFIG_CONFIGURE))
#
# liverpool =[
#       {
#         "interface": "FastEthernet0/1",
#         "ip_address": "198.51.100.42",
#         "subnet_mask": "string",
#         'mode': 'sh',
#         "duplex": "string"
#       }
#     ]
# print(templ.render(interfaces=liverpool))

def _parse_config(s: str | None = None, info: str | None = None):
    path = PATH_CONFIG_PARSE.joinpath(s)
    b = info.ttp_parse_output(str(path))
    print(info)
    return b[0]


def get_device_configuration(s: str | None = None, command: str | None = None):
    with Scrapli(**driver._settings) as ssh:
        print(PATH_CONFIG_PARSE)
        a = ssh.send_command(command)
        print(a.result)
        return _parse_config(s, a)


def configure_device(params: DeviceConfigurationData):
    configurations = params.configuration.model_dump(exclude_none=True)
    print(f'{configurations=}')
    templ = env.get_template('base.j2')
    commands = templ.render(configurations)
    print(commands)
    print(commands.split('\n'))


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
