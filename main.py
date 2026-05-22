from fastapi import FastAPI

from routes.patient_routes import router

from database.database import engine, Base
from models.patient_model import PatientPrediction

from models.admin_model import Admin

from routes.admin_routes import router as admin_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)

app.include_router(admin_router)