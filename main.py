from fastapi import FastAPI

from routes.patient_routes import router

app = FastAPI()

app.include_router(router)