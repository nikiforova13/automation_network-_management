from fastapi import APIRouter
from fastapi.requests import Request
from app.dependencies.configurations_device import (
    get_device_configuration,
    configure_device,
)
from enums.commands import ShowCommandsCisco
from routers.api_schemas.configuration import DeviceConfigurationData

router = APIRouter(prefix="/configuration", tags=["Device Configuration"])


@router.get("")
async def get_configuration(request: Request) -> DeviceConfigurationData:
    if request:
        return get_device_configuration(s="all", command=ShowCommandsCisco.ALL_CONFIG)


@router.post("")
async def create_configuration(params: DeviceConfigurationData):
    # print(params)
    return configure_device(params)


@router.patch("")
async def update_configuration(): ...


@router.delete("")
async def delete_configuration(): ...
