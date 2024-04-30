import typing

from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi import APIRouter, Depends, Form, Query

from app.routers.router import get_configuration

from app.dependencies.configurations_device import (
    get_device_configuration,
    subnet_masks_with_prefix,
)
from app.config.device_config import templates
from app.models.vlan import VlanOnDevice
from routers.api_schemas.configuration import (
    DeviceConfigurationData,
)

router = APIRouter(prefix="/ui/configuration", tags=["Ui-stub"])


@router.get("", response_class=HTMLResponse)
async def get_configuration(
    request: Request,
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
    print(f"{data=}")
    for k, v in data.items():
        print(k)
        print(v)
    # hostname = data.get('ip_address')
    # print(hostname)
    # data1 = []
    # vlan_on_device = []
    # vlan_names = [
    # ]
    # vlan_numbers = []
    # for key, value in data.items():
    #     print(key)
    #     print(value)
    #     if value == '':
    #         continue
    #     if key == 'vlan_name':
    #         vlan_names.append(value)
    #     if key == 'vlan_number':
    #         vlan_numbers.append(value)
    #
    #
    # print(vlan_numbers)
    # print(vlan_names)
    # a = VlanOnDevice(number=new.get('vlan_number'), name=new.get('vlan_name'))

    # print(a)
    # VlanOnInterface
    # ip_address =
    # a = CreateConfiguration(ip_address=new.get('ip_address'), hostname=new.get('hostname'))
    # print(a)
    return templates.TemplateResponse(
        name="configure.html",
        context={"request": request, "subnet_masks": subnet_masks_with_prefix()},
    )
