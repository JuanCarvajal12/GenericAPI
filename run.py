"""
@carva

when deving on VSCode in my machine, change interpreter with
(Ctrl+Shift+P) | >Python:Select Interpreter | 'fastapidev' conda

run with
      uvicorn run:app --reload --port 3000
--reload enables auto-refreshing when updating code.
"""

#%---
from fastapi import FastAPI, Depends, HTTPException
from routes.v1 import app_v1
from routes.v2 import app_v2
from routes.old import app_old
from starlette.requests import Request
from starlette.responses import Response
from starlette.status import HTTP_401_UNAUTHORIZED
from utils.security import check_jwt_token
from datetime import datetime
# Import authentication tools
from fastapi.security import OAuth2PasswordRequestForm
from utils.security import authenticate_user, create_jwt_token
from models.jwt_user import JWTUser
from utils.const import *
from utils.db_object import db
import utils.redis_obj as re
import aioredis

app = FastAPI(title="GenericAPI", description="Sample API with generic content\
       and multiple examples", version="0.0.1")

app.include_router(app_old, prefix="/old", dependencies=[Depends(check_jwt_token)])
app.include_router(app_v1, prefix="/v1", dependencies=[Depends(check_jwt_token)])
app.include_router(app_v2, prefix="/v2", dependencies=[Depends(check_jwt_token)])

@app.on_event("startup")
async def connect_db():
      await db.connect()
      re.redis = await aioredis.create_redis_pool(REDIS_URL)

@app.on_event("shutdown")
async def disconnect_db():
      await db.disconnect()
      re.redis.close()
      await re.redis.wait_closed()


# Authorization token generation endpoint

@app.post("/token", description=TOKEN_DESCRIPTION, summary=TOKEN_SUMMARY,
      tags=['Auth'])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    jwt_user_dict = {
        "username": form_data.username,
        "password": form_data.password
    }
    jwt_user = JWTUser(**jwt_user_dict)

    user = await authenticate_user(jwt_user)

    if user is None:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)

    jwt_token = create_jwt_token(user)
    return {'access_token': jwt_token}

@app.middleware("http")
async def middleware(request: Request, call_next):
      start_time = datetime.utcnow()
      # modify request

      """# Example: requiring auth on all requests with exceptions
      # This is a bad practice. If done in this manner, the swagger auto-gen
      # documentation will have flaws. I have a correct implementation using
      # APIRouter's.
      open_paths = ["/token", "/docs", "/openapi.json"]
      if not any(word in str(request.url) for word in open_paths):
            try:
                  jwt_token = request.headers['Authorization'].split(' ')[1]
                  is_valid = check_jwt_token(jwt_token)
            except Exception as e:
                  is_valid = False
            
            if not is_valid:
                  return Response("Unauthorized", status_code=HTTP_401_UNAUTHORIZED)
      """
      response = await call_next(request)

      execution_time = (datetime.utcnow() - start_time).microseconds
      response.headers["x-execution-time"] = str(execution_time)
      # modify response
      return response