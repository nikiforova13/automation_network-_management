from fastapi import APIRouter
from fastapi.requests import Request
from app.dependencies.configurations_device import (
    get_device_configuration,
    configure_device,
)
from routers.api_schemas.configuration import DeviceConfigurationData
from fastapi.responses import Response
router = APIRouter(prefix="/configuration", tags=["Device Configuration"])


@router.get("")
async def get_configuration() -> DeviceConfigurationData:
    return await get_device_configuration()


@router.post("")
async def create_configuration(params: DeviceConfigurationData) -> Response:
    return await configure_device(params)


@router.patch("")
async def update_configuration(params: DeviceConfigurationData) -> Response:
    return await configure_device(params)



@router.delete("")
async def delete_configuration(params: DeviceConfigurationData) -> Response:
    return await configure_device(params, action='delete')
