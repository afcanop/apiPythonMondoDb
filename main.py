from fastapi import FastAPI
from routes.logRouter import LogRouter

app = FastAPI()

app.include_router(LogRouter)