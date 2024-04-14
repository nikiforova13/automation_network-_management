from enum import StrEnum


class ShowCommandsCisco(StrEnum):
    ALL_CONFIG = "show running-config"
    INTERFACES = "show ip interface brief"
