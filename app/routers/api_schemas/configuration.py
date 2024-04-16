from pydantic import BaseModel
from ipaddress import IPv4Address, IPv4Network

from app.models.interfaces import Interface
from app.models.routing import Routing


class DeviceConfiguration(BaseModel):
    hostname: str | None = None
    interfaces: list[Interface] | None = None
    routing: Routing | None = None


class DeviceConfigurationData(BaseModel):
    configuration: DeviceConfiguration


class CreateConfiguration(BaseModel): ...
