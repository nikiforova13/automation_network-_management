from enum import StrEnum


class ShowCommandsCisco(StrEnum):
    ALL_CONFIG = "show run"
    INTERFACES = "show ip interface brief"
