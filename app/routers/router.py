from fastapi import APIRouter
from fastapi.requests import Request
from scrapli import Scrapli
from app.dependencies.configurations_device import get_device_configuration
from config.driver import driver
from enums.commands import ShowCommandsCisco

router = APIRouter(prefix="/configurations")


@router.get("/hello")
def hello():
    return "hello"


@router.get("/all")
def get_configurations(request: Request):
    if request:
        return get_device_configuration(s='all', command=ShowCommandsCisco.ALL_CONFIG)


@router.get("/interfaces")
def get_interfaces(request: Request):
    if request:
        return get_device_configuration('interfaces',command=ShowCommandsCisco.INTERFACES)
