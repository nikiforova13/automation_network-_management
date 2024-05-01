from fastapi import APIRouter
from app.dependencies.configurations_device import (
    get_device_configuration,
    configure_device,
)
from app.enums import configurations
from app.routers.api_schemas.configuration import DeviceConfigurationData
from fastapi.responses import Response

router = APIRouter(prefix="/configuration", tags=["Device Configuration"])


@router.get("/{hostname}")
async def get_configuration(hostname: str) -> DeviceConfigurationData:
    return await get_device_configuration(hostname)


@router.post("/{hostname}")
async def create_configuration(
    hostname: str, params: DeviceConfigurationData
) -> Response:
    return await configure_device(hostname, params)


@router.patch("/{hostname}")
async def update_configuration(
    hostname: str, params: DeviceConfigurationData
) -> Response:
    return await configure_device(hostname, params)


@router.delete("/{hostname}")
async def delete_configuration(
    hostname: str, params: DeviceConfigurationData
) -> Response:
    return await configure_device(hostname, params, action=configurations.Action.delete)
