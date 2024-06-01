from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from app.config.device_config import templates

router = APIRouter(prefix="")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        name="index.html",
        context={"request": request},
    )
