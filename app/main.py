import uvicorn
from fastapi import FastAPI
from app.routers import configurations_router
from app.ui_stub import configurations_ui_router, index_router

app = FastAPI()


app.include_router(index_router)
app.include_router(configurations_router)
app.include_router(configurations_ui_router)

if __name__ == "__main__":
    uvicorn.run(app=app, port=8001, host="127.0.0.1")
