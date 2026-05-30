from fastapi import FastAPI

from routes.patient_routes import router

from database.database import engine, Base
from models.patient_model import PatientPrediction

from models.admin_model import Admin

from routes.admin_routes import router as admin_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(router)

app.include_router(admin_router)