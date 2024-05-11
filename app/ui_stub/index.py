import pathlib

from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi import APIRouter

from fastapi.templating import Jinja2Templates

APP_GLOBAL_PATH = pathlib.Path(__file__).absolute().parent.parent.joinpath("templates")

router = APIRouter(prefix="")
templates = Jinja2Templates(directory=APP_GLOBAL_PATH)


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        name="index.html",
        context={"request": request},
    )
