from pydantic import BaseModel, ConfigDict


class BaseCase:
    model_config = ConfigDict(from_attributes=True)
