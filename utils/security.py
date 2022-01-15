"""
@Carva
"""

from passlib.context import CryptContext
from models.jwt_user import JWTUser
from datetime import datetime, timedelta
from utils.const import JWT_EXPIRATION_TIME_MINUTES, JWT_ALGORITHM, JWT_SECRET_KEY
import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import time
from starlette.status import HTTP_401_UNAUTHORIZED

pwd_context = CryptContext(schemes=['bcrypt'])
oauth_schema = OAuth2PasswordBearer(tokenUrl='/token')

jwt_user_sample = {
    'username': 'sample_user',
    'password': '$2b$12$HYmFBD9ekxfp5w/OAGfn2un1iCTgeG3buSJ10B/sOObHUlEhhdplu',
    'disabled': False,
    'role': 'admin'}
jwt_user_sample = JWTUser(**jwt_user_sample)


def get_hashed_password(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except Exception as e:
        return False

# Authenticate username and pw to gen JWT token

def authenticate_user(user: JWTUser):
    if jwt_user_sample.username == user.username:
        if verify_password(user.password,jwt_user_sample.password):
            user.role = 'admin'
            return user
    return None

# Create access JWT token
def create_jwt_token(user: JWTUser):
    exp_time = datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_TIME_MINUTES)
    jwt_payload = {
        "sub": user.username,
        "role": user.role,
        "exp": exp_time
    }
    jwt_token = jwt.encode(jwt_payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return jwt_token

# Verify JWT token
def check_jwt_token(token: str = Depends(oauth_schema)):
    try:
        jwt_payload = jwt.decode(token, JWT_SECRET_KEY, algorithms = JWT_ALGORITHM)
        username = jwt_payload.get("sub")
        role = jwt_payload.get("role")
        expiration = jwt_payload.get("exp")

        if time.time() < expiration:
            if jwt_user_sample.username == username:
                return final_checks(role)
    except Exception as e:
        return False
    
    return False

# Authorization
def final_checks(role: str):
    if role == "admin":
        return True
    else:
        return False
