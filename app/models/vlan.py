from pydantic import BaseModel


class VlanOnInterface(BaseModel):
    number: int | None = None
    mode: str | None = None


class VlanOnDevice(BaseModel):
    number: int | None = None
    name: str | None = None
