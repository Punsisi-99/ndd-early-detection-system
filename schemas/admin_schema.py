from pydantic import BaseModel

class AdminCreate(BaseModel):   #validate admin registration data
    username: str
    password: str