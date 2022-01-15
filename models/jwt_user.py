from pydantic import BaseModel



# jwt_user class
class JWTUser(BaseModel):
    username: str
    password: str
    disabled: bool = False
    role: str = None