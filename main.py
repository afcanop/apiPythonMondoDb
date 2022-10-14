from fastapi import FastAPI
from routes.logRouter import LogRouter

app = FastAPI(
    title="apiLogCromo",
    description="Apis para el control del log de erp semantica"
)

app.include_router(LogRouter)