"""
@carva

when deving on VSCode in my machine, change interpreter with
(Ctrl+Shift+P) | >Python:Select Interpreter | 'fastapidev' conda

version 2. Further learning about FastAPI.
"""

#%---
from fastapi.param_functions import Header, Depends
from models.user import User
from models.product import Product
from models.supplier import Supplier
from fastapi import FastAPI, Header, File, Body
from starlette.status import HTTP_201_CREATED # Import necessary status codes.
from starlette.responses import Response

from utils.security import check_jwt_token

#%---
app_v2 = FastAPI(root_path='/v2')

#%---
# POST /user
# IMPORTANT: In python i wrote 'x_custom', but in the request I use 'x-custom'.
## ADDED FUNCTIONALITY: Now this function requires authentication and authori-
## zation. In the header of the request, should appear the Authorization entry
## with value "Bearer <token>". The token is generated with POST -> /v1/token.
@app_v2.post("/user", status_code=HTTP_201_CREATED) # endpoint
async def post_user(user: User, x_custom: str = Header("default value"), jwt: bool = Depends(check_jwt_token)):
    return {"request body": {'user': user, "version": 'v2'},
            "request custom header": x_custom}