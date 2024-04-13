from pydantic import Field, field_validator, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict
from ipaddress import IPv4Address
from typing import Literal, Any
from config.base import get_updated_model_config, BASE_CONFIG


class BaseNetworkDriverSettings(BaseSettings):
    model_config = SettingsConfigDict(
        get_updated_model_config(BASE_CONFIG, SettingsConfigDict(env_prefix="DEVICE_"))
    )
    host: str
    platform: str = Literal[
        "cisco_iosxe", "arista_eos", "cisco_iosxr", "cisco_nxos", "juniper_junos"
    ]
    transport: str = Field(default="paramiko")
    auth_username: str
    auth_password: str
    auth_secondary: str
    auth_strict_key: bool

    @field_validator("host")
    @classmethod
    def check_ipaddress(cls, v: Any):
        try:
            IPv4Address(v)
        except (ValidationError, ValueError):
            raise TypeError("Invalid IP address format")
        return v

    @property
    def _settings(self):
        return self.model_dump()


driver = BaseNetworkDriverSettings()
