from fastapi import APIRouter
from fastapi.requests import Request
from scrapli import Scrapli

from config.driver import driver
import pathlib

PATH_CONFIG_PARSE = (
    pathlib.Path(__file__)
    .absolute()
    .parent.parent.joinpath("templates_device")
    .joinpath("parse_config")
)


def _parse_config(s: str | None = None, info: str | None = None):
    if s:
        PATH_CONFIG_PARSE.joinpath(s)
    b = info.ttp_parse_output(str(PATH_CONFIG_PARSE))
    return b


def get_device_configuration(s: str | None = None, command: str | None = None):
    with Scrapli(**driver._settings) as ssh:
        print(PATH_CONFIG_PARSE)
        a = ssh.send_command(command)
        return _parse_config(s, a)
