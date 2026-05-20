import joblib
import numpy as np
from pytorch_tabnet.tab_model import TabNetClassifier 

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
feature_importances = joblib.load("feature_importances.pkl")

def predict_patient(patient):

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

    #reasons for the prediction
    reason_scores = []

    for name, value, importance in zip(feature_names, features, feature_importances):
        if value == 1:
            reason_scores.append({
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