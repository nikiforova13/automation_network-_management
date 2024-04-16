from pydantic_settings import SettingsConfigDict
import pathlib

APP_GLOBAL_PATH = pathlib.Path(__file__).absolute().parent.parent
BASE_CONFIG: SettingsConfigDict = SettingsConfigDict(
    env_file=APP_GLOBAL_PATH.joinpath(".env"), env_file_encoding="utf-8"
)


def get_updated_model_config(orig: SettingsConfigDict, update: SettingsConfigDict):
    copy = orig.copy()
    for key, value in update.items():
        copy[key] = value
    return copy
