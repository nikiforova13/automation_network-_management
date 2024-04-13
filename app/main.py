import uvicorn
from fastapi import FastAPI
from app.routers import configurations_router

app = FastAPI()

app.include_router(configurations_router)

if __name__ == "__main__":
    uvicorn.run(app=app, port=8000, host="127.0.0.1")
