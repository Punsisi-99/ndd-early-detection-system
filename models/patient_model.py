from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from database.database import Base

class PatientPrediction(Base):

    __tablename__ = "patient_predictions_Database"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    family_history = Column(String, nullable=False)
    inattention = Column(String, nullable=False)
    easily_distracted = Column(String, nullable=False)
    poor_response = Column(String, nullable=False)
    social_interaction_difficulty = Column(String, nullable=False)
    communication_issues = Column(String, nullable=False)
    poor_task_engagement = Column(String, nullable=False)
    excessive_talking = Column(String, nullable=False)
    hyperactivity = Column(String, nullable=False)
    risk_taking_behavior = Column(String, nullable=False)
    forgetfulness = Column(String, nullable=False)
    impulsivity = Column(String, nullable=False)
    aggressive = Column(String, nullable=False)
    lack_of_empathy = Column(String, nullable=False)
    pretend_play = Column(String, nullable=False)
    eye_contact_or_joint_attention = Column(String, nullable=False)
    deficits_pointing = Column(String, nullable=False)
    restrictive_repetitive_movements = Column(String, nullable=False)
    response_to_name = Column(String, nullable=False)
    diagnosis = Column(String, nullable=False)
    prediction_code = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

