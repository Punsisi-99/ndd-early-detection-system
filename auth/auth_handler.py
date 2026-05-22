from jose import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext    #fro password hashing system

from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

outh2_scheme = OAuth2PasswordBearer(tokenUrl="login")  #token URL for admin login

# Secret key
SECRET_KEY = "your_secret_key"

#JWT algorithm
ALGORITHM = "HS256"

#Token expiration time (in minutes)
ACCESS_TOKEN_EXPIRE_MINUTES = 60

#password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#Hash password
def hash_password(password: str):   #encrypt admin password (like $2b$12$asdasdasdadasd...)
    return pwd_context.hash(password)

#Verify password
def verify_password(plain_password, hashed_password):   #check login password with hashed password
    return pwd_context.verify(plain_password, hashed_password)

#Create JWT token
def create_access_token(data:dict):     #generate JWT token for admin

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(         # current time + 1 hr
        minutes = ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm = ALGORITHM
    )

    return encoded_jwt

def verify_token(token: str = Depends(outh2_scheme)):   #verify JWT token for protected routes

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms = [ALGORITHM]
        )

        username = payload.get("sub")

        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return username

    except:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )