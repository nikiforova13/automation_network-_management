from fastapi import APIRouter
from app.dependencies.configurations_device import (
    get_device_configuration,
    configure_device,
    configure_devices,
)
from app.enums import configurations
from app.routers.api_schemas.configuration import (
    DeviceConfigurationData,
    BatchDeviceConfigurationData,
)
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


# @router.get("/devices")
# async def batch_configuration(params: BatchSearchDevice) -> Response:
#     return await get_device_configuration(params)


@router.patch("/devices")
async def batch_update_configuration(params: BatchDeviceConfigurationData) -> Response:
    return await configure_devices(params)


@router.post("/devices")
async def batch_create_configuration(params: BatchDeviceConfigurationData) -> Response:
    return await configure_devices(params)


@router.delete("/devices")
async def batch_delete_configuration(params: BatchDeviceConfigurationData) -> Response:
    return await configure_devices(params, action=configurations.Action.delete)
