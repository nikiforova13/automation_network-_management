from pydantic import BaseModel
from app.routers.api_schemas.base import BaseCase


class VlanOnInterface(BaseModel, BaseCase):
    number: int | None = None
    mode: str | None = None


class VlanOnDevice(BaseModel, BaseCase):
    number: int | None = None
    name: str | None = None
