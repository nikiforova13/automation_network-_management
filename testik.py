from pydantic import BaseModel, ConfigDict
from ipaddress import IPv4Address, IPv4Network
from app.routers.api_schemas.base import BaseCase
from pydantic import BeforeValidator, AfterValidator
import typing


class StaticRoutes(BaseModel):
    destination: typing.Annotated[str, BeforeValidator(is_ip_network)]


a = StaticRoutes(destination="sf")
print(a)
