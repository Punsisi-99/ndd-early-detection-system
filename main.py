from fastapi import FastAPI
from pydantic import BaseModel

import joblib
import numpy as np
from pytorch_tabnet.tab_model import TabNetClassifier

app = FastAPI()


#load scaler
scaler = joblib.load("scaler.pkl")

#load trained model
model = TabNetClassifier()
model.load_model("tabnet_ndd_model.zip")

#prediction labels
diagnosis_labels = {
    0: "Healthy",
    1: "ASD",
    2: "ADHD"
}

#feature importance
feature_names = [
    "Family_History",
    "Inattention",
    "Easily_Distracted",
    "Poor_response",
    "Social_Interaction_Difficulty",
    "Communication_Issues",
    "Poor_Task_Engagement",
    "Excessive_Talking",
    "Hyperactivity",
    "Risk_Taking_Behavior",
    "Forgetfulness",
    "Impulsivity",
    "Aggressive_(Difficult_Waiting_Turns)",
    "Lack_of_Empathy",
    "Pretend_Play",
    "Eye_Contact_or_Joint_Attention",
    "Deficits_Pointing",
    "Restrictive_Repetative_Movments",
    "Response_to_Name"
]

feature_importances = model.feature_importances_

#Patient data model
class Patient(BaseModel):
    name: str
    age_months: int
    gender: str
    family_history: str
    inattention : str
    easily_distracted : str
    poor_response: str
    social_interaction_difficulty: str
    communication_issues: str
    poor_task_engagement: str
    excessive_talking: str
    hyperactivity: str
    risk_taking_behavior: str
    forgetfulness: str
    impulsivity: str
    aggressive: str
    lack_of_empathy: str
    pretend_play: str
    eye_contact_or_joint_attention: str
    deficits_pointing: str
    restrictive_repetitive_movements: str
    response_to_name: str

#Get route
@app.get("/")
def home():
    return {"message": "Hello,Your backend is working!"}

@app.get("/about")
def about():
    return {"Project" : "NDD Early Detection System",
            "Developer" : "Punsisi Chamoda"}

#POST request
@app.post("/patient")
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

@app.post("/predict")
def predict (patient : Patient):
    # Here you would typically load your trained model and make a prediction based on the patient's data
    
    gender_value = 1 if patient.gender.lower() == "male" else 0

    features = [
        1 if patient.family_history.lower() == "yes" else 0,
        1 if patient.inattention.lower() == "yes" else 0,
        1 if patient.easily_distracted.lower() == "yes" else 0,
        1 if patient.poor_response.lower() == "yes" else 0,
        1 if patient.social_interaction_difficulty.lower() == "yes" else 0,
        1 if patient.communication_issues.lower() == "yes" else 0,
        1 if patient.poor_task_engagement.lower() == "yes" else 0,
        1 if patient.excessive_talking.lower() == "yes" else 0,
        1 if patient.hyperactivity.lower() == "yes" else 0,
        1 if patient.risk_taking_behavior.lower() == "yes" else 0,
        1 if patient.forgetfulness.lower() == "yes" else 0,
        1 if patient.impulsivity.lower() == "yes" else 0,
        1 if patient.aggressive.lower() == "yes" else 0,
        1 if patient.lack_of_empathy.lower() == "yes" else 0,
        1 if patient.pretend_play.lower() == "no" else 0,
        1 if patient.eye_contact_or_joint_attention.lower() == "no" else 0,
        1 if patient.deficits_pointing.lower() == "yes" else 0,
        1 if patient.restrictive_repetitive_movements.lower() == "yes" else 0,
        1 if patient.response_to_name.lower() == "no" else 0
    ]

    input_array = np.array([features])
    input_scaled = scaler.transform(input_array)

    prediction = model.predict(input_scaled)
    prediction_class = int(prediction[0])
    diagnosis = diagnosis_labels[prediction_class]

    #if healthy
    if diagnosis == "Healthy":
        return {
            "message" : "Prediction completed successfully",
            "prediction_code" : prediction_class,
            "diagnosis" : diagnosis,
            "reason" : "There are no identified symptoms of ASD or ADHD"
        }

    #source reasons for the prediction
    reason_source = []

    for name, value, importance in zip(feature_names, features, feature_importances):
        if value == 1:
            reason_source.append({
                "symptom" : name,
                "importance_score" : float(importance)
            })

    reason_scores = sorted(
        reason_scores,
        key = lambda x: x["importance_score"],
        reverse = True
    )

    main_reasons = reason_scores[:5]

    return {
        "message" : "Prediction completed successfully",
        "prediction_code": prediction_class,
        "diagnosis": diagnosis,
        "main_reasons": main_reasons
    }