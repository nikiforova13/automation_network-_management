from pydantic import BaseModel, ConfigDict
from ipaddress import IPv4Address, IPv4Network

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


class CreateConfiguration(DeviceConfiguration):
    ip_address: IPv4Address | None = None
