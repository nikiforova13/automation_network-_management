import typing
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi import APIRouter, Query
from app.dependencies.configurations_device import (
    get_device_configuration,
    configure_device,
)
from app.config.device_config import templates
from app.models.vlan import VlanOnDevice
from app.routers.api_schemas.configuration import (
    DeviceConfigurationData,
    DeviceConfiguration,
)
from app.models.interfaces import Interface
from app.models.routing import Routing, StaticRoutes, OSPF, NetworkByArea
from app.dependencies.tools import subnet_masks

router = APIRouter(prefix="/ui/configuration", tags=["Ui-stub"])


@router.get("", response_class=HTMLResponse)
async def get_configuration(
    request: Request,
    hostname: typing.Annotated[str | None, Query()] = None,
):
    config = ""
    if hostname:
        config = await get_device_configuration(hostname)
    return templates.TemplateResponse(
        name="device.html",
        context={"request": request, "configurations": config},
    )


@router.get("/create", response_class=HTMLResponse)
async def create_configuration(request: Request):
    return templates.TemplateResponse(
        name="configure.html",
        context={"request": request, "subnet_masks": subnet_masks()},
    )


@router.post("/create", response_class=HTMLResponse)
async def create_configuration(request: Request):
    data = await request.form()
    obj = {k: v for k, v in data.items() if v not in ("", "-")}
    vlans = [VlanOnDevice(number=obj.get("vlan_number"), name=obj.get("vlan_name"))]
    interfaces = [
        Interface(
            interface=obj.get("interface"),
            address=obj.get("address"),
            subnet_mask=obj.get("subnet_mask"),
            status=obj.get("status"),
            vlan=None,
        )
    ]
    routing = Routing(
        static=[
            StaticRoutes(
                destination=obj.get("destination"),
                subnet_mask=obj.get("subnet_mask_dst"),
                next_hop=obj.get("next_hop"),
            )
        ],
        ospf=OSPF(
            router_id=obj.get("OSPF"),
            networks=[
                NetworkByArea(
                    network=obj.get("network"),
                    subnet_mask=obj.get("subnet_mask_ospf"),
                    area=obj.get("area"),
                )
            ],
        ),
    )
    config = DeviceConfigurationData(
        configuration=DeviceConfiguration(
            hostname=data.get("hostname"),
            vlans=vlans,
            interfaces=interfaces,
            routing=routing,
        )
    )
    try:
        await configure_device(data.get("hostname"), config)
    except Exception as err:
        message = err
    return templates.TemplateResponse(
        name="configure.html",
        context={
            "request": request,
            "subnet_masks": subnet_masks(),
            "message": message,
        },
    )
