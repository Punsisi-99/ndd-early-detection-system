from fastapi import FastAPI

from routes.patient_routes import router

from database.database import engine, Base
from models.patient_model import PatientPrediction

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)