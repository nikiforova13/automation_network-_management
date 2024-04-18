import pathlib
import typing

from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi import APIRouter, Depends

from app.routers.router import get_configuration
from fastapi.templating import Jinja2Templates

from routers.api_schemas.configuration import DeviceConfigurationData

APP_GLOBAL_PATH = pathlib.Path(__file__).absolute().parent.parent.joinpath("templates")

router = APIRouter(prefix="/configuration/ui")

templates = Jinja2Templates(directory=APP_GLOBAL_PATH)


@router.get("", response_class=HTMLResponse)
async def get_configuration(
    request: Request,
    config: typing.Annotated[DeviceConfigurationData, Depends(get_configuration)],
):
    print(config)
    return templates.TemplateResponse(
        name="device.html",
        context={"request": request, "configurations": config},
    )
