from pydantic import BaseModel
from ipaddress import IPv4Address, IPv4Network
from app.routers.api_schemas.base import BaseCase
from pydantic import BeforeValidator
import typing


def is_ip_network(v: str):
    try:
        IPv4Network(v)
    except ValueError as err:
        ...
    else:
        return v


def is_ip_address(v: str):
    try:
        IPv4Address(v)
    except ValueError as err:
        ...
    else:
        return v


class StaticRoutes(BaseModel, BaseCase):
    destination: typing.Annotated[str, BeforeValidator(is_ip_network)] | None = None
    subnet_mask: str | None = None
    next_hop: typing.Annotated[str, BeforeValidator(is_ip_address)] | None = None


class NetworkByArea(BaseModel, BaseCase):
    network: typing.Annotated[str, BeforeValidator(is_ip_network)] | None = None
    subnet_mask: str | None = None
    area: int | None = None


class OSPF(BaseModel, BaseCase):
    networks: list[NetworkByArea] | NetworkByArea
    router_id: str | None = None


class Routing(BaseModel, BaseCase):
    static: list[StaticRoutes] | None = None
    ospf: OSPF | None = None
