from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer   #This API uses Bearer Token authentication and Users can obtain tokens from /login endpoint.
from jose import jwt, JWTError

from database.database import SessionLocal
from models.admin_model import Admin
from auth.auth_handler import SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_admin(token: str = Depends(oauth2_scheme)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials"
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        username = payload.get("sub")

        if username is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    db = SessionLocal()

    admin = db.query(Admin).filter(Admin.username == username).first()

    db.close()

    if admin is None:
        raise credentials_exception

    return admin