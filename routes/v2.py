"""
@carva

when deving on VSCode in my machine, change interpreter with
(Ctrl+Shift+P) | >Python:Select Interpreter | 'fastapidev' conda

version 2. Further learning about FastAPI.
"""

#%---
from fastapi.param_functions import Header
from models.user import User
from models.product import Product
from models.supplier import Supplier
from fastapi import FastAPI, Header, File, Body
from starlette.status import HTTP_201_CREATED # Import necessary status codes.
from starlette.responses import Response

#%---
app_v2 = FastAPI(openapi_prefix='/v2')

#%---
# POST /user
# IMPORTANT: In python i wrote 'x_custom', but in the request I use 'x-custom'.
@app_v2.post("/user", status_code=HTTP_201_CREATED) # endpoint
async def post_user(user: User, x_custom: str = Header("default value")):
    return {"request body": {'user': user, "version": 'v2'},
            "request custom header": x_custom}