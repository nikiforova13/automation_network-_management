from fastapi import APIRouter
from fastapi.responses import Response

from app.dependencies.configurations_device import (
    configure_device,
    configure_devices,
    get_device_configuration,
)
from app.enums import configurations
from app.routers.api_schemas.configuration import (
    BatchDeviceConfigurationData,
    DeviceConfigurationData,
)
from app.routers.api_schemas.base import BaseAPIResponse

router = APIRouter(prefix="/configuration", tags=["Device Configuration"])


@router.get("/{hostname}", responses=BaseAPIResponse)
async def get_configuration(hostname: str) -> DeviceConfigurationData:
    return await get_device_configuration(hostname)


@router.post("/{hostname}", responses=BaseAPIResponse)
async def create_configuration(
    hostname: str, params: DeviceConfigurationData
) -> Response:
    return await configure_device(hostname, params)


@router.patch("/{hostname}", responses=BaseAPIResponse)
async def update_configuration(
    hostname: str, params: DeviceConfigurationData
) -> Response:
    return await configure_device(hostname, params)


@router.delete("/{hostname}", responses=BaseAPIResponse)
async def delete_configuration(
    hostname: str, params: DeviceConfigurationData
) -> Response:
    return await configure_device(
        hostname, params, action=configurations.ActionConfiguration.delete
    )


# @router.get("/devices")
# async def batch_configuration(params: BatchSearchDevice) -> Response:
#     return await get_device_configuration(params)


@router.patch("/devices", responses=BaseAPIResponse)
async def batch_update_configuration(params: BatchDeviceConfigurationData) -> Response:
    return await configure_devices(params)


@router.post("/devices", responses=BaseAPIResponse)
async def batch_create_configuration(params: BatchDeviceConfigurationData) -> Response:
    return await configure_devices(params)


@router.delete("/devices", responses=BaseAPIResponse)
async def batch_delete_configuration(params: BatchDeviceConfigurationData) -> Response:
    return await configure_devices(
        params, action=configurations.ActionConfiguration.delete
    )
