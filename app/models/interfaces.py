from pydantic import BaseModel
from ipaddress import IPv4Address, IPv4Network


class Vlan(BaseModel):
    number: int | None = None
    mode: str | None = None


class Interface(BaseModel):
    interface: str | None = None
    ip_address: IPv4Address | None = None
    subnet_mask: str | None = None
    status: str | None = None
    duplex: str | None = None
    vlan: Vlan | None = None
