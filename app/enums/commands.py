from enum import StrEnum


class ShowCommandCisco(StrEnum):
    ALL_CONFIG = "show running-config"
    INTERFACES = "show ip interface brief"
