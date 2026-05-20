from fastapi import APIRouter

from schemas.patient_schema import Patient
from services.prediction_service import predict_patient

from sqlalchemy.orm import Session
from fastapi import Depends
from database.database import get_db

from models.patient_model import PatientPrediction

from schemas.response_schema import PredictionResponse

router = APIRouter()

#Get route
@router.get("/")
def home():
    return {"message": "Hello,Your backend is working!"}

@router.get("/about")
def about():
    return {"Project" : "NDD Early Detection System",
            "Developer" : "Punsisi Chamoda"}

#POST request
@router.post("/patient")
def create_patient(patient: Patient):

    gender_value = 1 if patient.gender.lower() == "male" else 0

    symptom_data = {
        "gender": gender_value,
        "family_history": 1 if patient.family_history.lower() == "yes" else 0,
        "inattention": 1 if patient.inattention.lower() == "yes" else 0,
        "easily_distracted": 1 if patient.easily_distracted.lower() == "yes" else 0,
        "poor_response": 1 if patient.poor_response.lower() == "yes" else 0,
        "social_interaction_difficulty": 1 if patient.social_interaction_difficulty.lower() == "yes" else 0,
        "communication_issues": 1 if patient.communication_issues.lower() == "yes" else 0,
        "poor_task_engagement": 1 if patient.poor_task_engagement.lower() == "yes" else 0,
        "excessive_talking": 1 if patient.excessive_talking.lower() == "yes" else 0,
        "hyperactivity": 1 if patient.hyperactivity.lower() == "yes" else 0,
        "risk_taking_behavior": 1 if patient.risk_taking_behavior.lower() == "yes" else 0,
        "forgetfulness": 1 if patient.forgetfulness.lower() == "yes" else 0,
        "impulsivity": 1 if patient.impulsivity.lower() == "yes" else 0,
        "aggressive": 1 if patient.aggressive.lower() == "yes" else 0,
        "lack_of_empathy": 1 if patient.lack_of_empathy.lower() == "yes" else 0,
        "pretend_play": 1 if patient.pretend_play.lower() == "no" else 0,
        "eye_contact_or_joint_attention": 1 if patient.eye_contact_or_joint_attention.lower() == "no" else 0,
        "deficits_pointing": 1 if patient.deficits_pointing.lower() == "yes" else 0,
        "restrictive_repetitive_movements": 1 if patient.restrictive_repetitive_movements.lower() == "yes" else 0,
        "response_to_name": 1 if patient.response_to_name.lower() == "no" else 0
    }
    return {"message" : "Patient processed successfully",
            "converted_data" : symptom_data}

@router.post("/predict")
def predict (patient : Patient, db: Session = Depends(get_db)):

    return predict_patient(patient, db)

@router.get("/predictions", response_model = list[PredictionResponse])
def get_predictions(db: Session = Depends(get_db)):
    predictions = db.query(PatientPrediction).all()

    return predictions