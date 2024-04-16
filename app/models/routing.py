from pydantic import BaseModel
from ipaddress import IPv4Address, IPv4Network


class StaticRoutes(BaseModel):
    destination: IPv4Network | None = None
    subnet_mask: str | None = None
    next_hop: IPv4Address | None = None


class OSPF(BaseModel): ...


class Routing(BaseModel):
    static: list[StaticRoutes] | None = None
    ospf: list[OSPF] | None = None
