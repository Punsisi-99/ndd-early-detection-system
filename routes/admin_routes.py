from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database.database import get_db
from schemas.admin_schema import AdminCreate
from models.admin_model import Admin

from auth.auth_handler import (
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter()

#Register admin
@router.post("/register")   #create admin account
def admin_register(admin: AdminCreate, db: Session = Depends(get_db)):

    hashed_password = hash_password(admin.password)

    new_admin =Admin(
        username =admin.username,
        password = hashed_password
    )

    db.add(new_admin)

    db.commit()

    db.refresh(new_admin)

    return {
        "message" : "Admin registered successfully"
    }

#Admin login
@router.post("/login")      #admin login and JWT token generation for authentication and authorization in protected routes
def admin_login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)):

    existing_admin = db.query(Admin).filter(
        Admin.username == form_data.username
    ).first()

    if not existing_admin:
        return {
            "error": "Invalid Username"
        }

    if not verify_password(form_data.password, existing_admin.password):
        return{
            "error": "Invalid Password"
        }
    
    access_token = create_access_token(
        data = {"sub": form_data.username}
    )

    return {
        "message": "Login successful",
        "access_token": access_token,
        "token_type": "bearer"
    }