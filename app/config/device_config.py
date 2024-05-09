import pathlib

from jinja2 import Environment, FileSystemLoader
from fastapi.templating import Jinja2Templates

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


path_html_templates = (
    pathlib.Path(__file__).absolute().parent.parent.joinpath("templates")
)

templates = Jinja2Templates(directory=path_html_templates)
