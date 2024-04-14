from pydantic import BaseModel
from ipaddress import IPv4Address, IPv4Network


class Routing(BaseModel):
    destination: IPv4Network | None = None
    subnet_mask: str | None = None
    next_hop: IPv4Address | None = None