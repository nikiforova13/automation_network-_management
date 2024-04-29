import pathlib
import typing

from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi import APIRouter, Depends, Form, Query

from app.routers.router import get_configuration
from fastapi.templating import Jinja2Templates

from app.dependencies.configurations_device import (
    get_device_configuration,
    subnet_masks_with_prefix,
)
from routers.api_schemas.configuration import DeviceConfigurationData

APP_GLOBAL_PATH = pathlib.Path(__file__).absolute().parent.parent.joinpath("templates")

router = APIRouter(prefix="/ui/configuration", tags=["Ui-stub"])

templates = Jinja2Templates(directory=APP_GLOBAL_PATH)


@router.get("", response_class=HTMLResponse)
async def get_configuration(
    request: Request,
    # config: typing.Annotated[DeviceConfigurationData, Depends(get_configuration)],
    hostname: typing.Annotated[str | None, Query()] = None,
):
    config = None
    if hostname:
        config = await get_device_configuration()
    return templates.TemplateResponse(
        name="device.html",
        context={"request": request, "configurations": config},
    )


@router.get("/create", response_class=HTMLResponse)
async def create_configuration(request: Request):
    return templates.TemplateResponse(
        name="configure.html",
        context={"request": request, "subnet_masks": subnet_masks_with_prefix()},
    )


@router.post("/create", response_class=HTMLResponse)
async def create_configuration(request: Request):
    data = await request.form()
    print(data)
    return templates.TemplateResponse(
        name="configure.html",
        context={"request": request, "subnet_masks": subnet_masks_with_prefix()},
    )
