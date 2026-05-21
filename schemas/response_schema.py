from pydantic import BaseModel
from datetime import datetime

class PredictionResponse(BaseModel):
    id: int
    name: str
    gender: str
    family_history: str
    inattention: str
    easily_distracted: str
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
    diagnosis: str
    prediction_code: int
    created_at: datetime

    class Config:
        from_attributes = True