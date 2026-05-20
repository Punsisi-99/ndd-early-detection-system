from typing import Literal
from pydantic import BaseModel, Field

#Patient data model
class Patient(BaseModel):
    name: str
    age_months: int = Field(..., ge = 6, le = 36) # age in months between 6 to 36
    gender: Literal["male","female"]
    family_history: Literal["yes", "no"]
    inattention : Literal["yes", "no"]
    easily_distracted : Literal["yes", "no"]
    poor_response: Literal["yes", "no"]
    social_interaction_difficulty: Literal["yes", "no"]
    communication_issues: Literal["yes", "no"]
    poor_task_engagement: Literal["yes", "no"]
    excessive_talking: Literal["yes", "no"]
    hyperactivity: Literal["yes", "no"]
    risk_taking_behavior: Literal["yes", "no"]
    forgetfulness: Literal["yes", "no"]
    impulsivity: Literal["yes", "no"]
    aggressive: Literal["yes", "no"]
    lack_of_empathy: Literal["yes", "no"]
    pretend_play: Literal["yes", "no"]
    eye_contact_or_joint_attention: Literal["yes", "no"]
    deficits_pointing: Literal["yes", "no"]
    restrictive_repetitive_movements: Literal["yes", "no"]
    response_to_name: Literal["yes", "no"]