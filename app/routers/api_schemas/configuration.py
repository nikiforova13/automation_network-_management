from pydantic import BaseModel

from app.models.interfaces import Interface
from app.models.routing import Routing
from app.models.vlan import VlanOnDevice
from app.routers.api_schemas.base import BaseCase


class DeviceConfiguration(BaseModel, BaseCase):
    hostname: str | None = None
    vlans: list[VlanOnDevice] | None = None
    interfaces: list[Interface] | None = None
    routing: Routing | None = None


class DeviceConfigurationData(BaseModel, BaseCase):
    configuration: DeviceConfiguration


class BatchDeviceConfigurationData(BaseModel, BaseCase):
    configurations: DeviceConfigurationData


class BatchSearchDevice(BaseModel, BaseCase):
    country: str | None = None
    city: str | None = None
    tag: str | None = None
    type_device: str | None = None
