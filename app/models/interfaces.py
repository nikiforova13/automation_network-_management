from pydantic import BaseModel
from ipaddress import IPv4Address, IPv4Network

from app.models.vlan import VlanOnInterface
from app.routers.api_schemas.base import BaseCase


class Interface(BaseModel, BaseCase):
    interface: str | None = None
    ip_address: IPv4Address | None = None
    subnet_mask: str | None = None
    status: str | None = "no shutdown"
    duplex: str | None = None
    vlan: VlanOnInterface | None = None
