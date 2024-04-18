from pydantic import BaseModel
from ipaddress import IPv4Address, IPv4Network
from app.routers.api_schemas.base import BaseCase


class StaticRoutes(BaseModel, BaseCase):
    destination: IPv4Network | None = None
    subnet_mask: str | None = None
    next_hop: IPv4Address | None = None


class OSPF(BaseModel, BaseCase): ...


class Routing(BaseModel, BaseCase):
    static: list[StaticRoutes] | None = None
    ospf: list[OSPF] | None = None
