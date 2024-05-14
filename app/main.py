import uvicorn
from fastapi import FastAPI
import sentry_sdk

from app.routers import configurations_router
from app.ui_stub import configurations_ui_router, index_router
from app.config.driver import settings

app = FastAPI()

sentry_sdk.init(
    dsn=settings.DSN,
    enable_tracing=True,
    traces_sample_rate=1.0,
)
app.include_router(index_router)
app.include_router(configurations_router)
app.include_router(configurations_ui_router)

if __name__ == "__main__":
    uvicorn.run(app=app, port=8001, host="127.0.0.1")
