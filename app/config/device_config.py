import pathlib
from app.routers.api_schemas.configuration import DeviceConfigurationData

from jinja2 import Environment, FileSystemLoader

path_config_parse = (
    pathlib.Path(__file__)
    .absolute()
    .parent.parent.joinpath("templates_device")
    .joinpath("parse_config")
    .joinpath("all")
)


path_configure_device = (
    pathlib.Path(__file__)
    .absolute()
    .parent.parent.joinpath("templates_device")
    .joinpath("configure_config")
)

env = Environment(loader=FileSystemLoader(path_configure_device))
template = env.get_template("base.j2")
