"""
@carva

This file was born as a copy of the initial version of the run.py.

when deving on VSCode in my machine, change interpreter with
(Ctrl+Shift+P) | >Python:Select Interpreter | 'fastapidev' conda

In this examples for each of the requests I'm just printing the
parameters, at first. I'm aware in the middle I can do whatever
I want with python as long as I return an appropriate result.
"""

#%---
from fastapi.param_functions import Header
from models.user import User
from models.product import Product
from models.supplier import Supplier
from fastapi import FastAPI, Header, File

# Import necessary status codes.
from starlette.status import HTTP_201_CREATED
from starlette.responses import Response

# This `Body` function allows a variable to be treated as an object,
# which enables it to be passed in a POST request as a JSON object.
# The parameter "embed" is neccesary under reasons explicit on "embed".
from fastapi import Body

#%---
app_v1 = FastAPI(openapi_prefix='/v1')

#%---

#%---

# POST /user 
# IMPORTANT: This is updated below, on advanced cases.
#@app_v1.post("/user") # endpoint
#async def post_user(user: User):
#    return {"request body": user}

#%---
# Two different types of GET requests:

## GET /user?password
### this version takes the argument as a query parameter
@app_v1.get("/user") # /user?password=*****
async def get_user_validation(password:str):
    return {"query parameter": password}

#%---
## GET /product/{ref}
## this option takes the argument as a path (or an enpoint?)
## this is just the base. Below, in advance cases, is an implementation
## of what the func name indicates should do
#@app_v1.get("/product/{ref}")
#async def get_product_with_ref(ref:str):
#    return {"query path parameter": ref}

#%---
# A combination of these two types into one path+query

## GET /supplier/{id}/product?year&category&order
## This would mean I want to query the products that fall in some 
## category and year, from a supplier with a specific id, in a certain
## order.
@app_v1.get("/supplier/{id}/product")
async def get_suppliers_products(id: int, year:int, category:str, order: str = 'asc'):
    return {"query parameters": str(id)+' '+str(year)+' '+category+' '+order}

#%---
# PATCH /supplier/name
@app_v1.patch("/supplier/name")
async def patch_supplier_name(name: str = Body(...,embed=True)):
    # we set embed=True so that I can pass the parameter 'name' as a JSON
    return {"name in body": name}

#%---
# POST /user/supplier
# This takes both the supplier and the product as parameters for the POST request.
# This takes an additional dummy parameter to show the incorporation of a variable
# in the request.
@app_v1.post("/user/supplier")
async def post_user_and_author(user: User, supplier: Supplier, dummy_param:str = Body(...,embed=True)):
    return {'user': user, 'supplier': supplier, 'dummy_param': dummy_param}

#%---
# NEW BLOCK: Advanced cases

#%---
# POST /user
# IMPORTANT: In python i wrote 'x_custom', but in the request I use 'x-custom'.
@app_v1.post("/user", status_code=HTTP_201_CREATED) # endpoint
async def post_user(user: User, x_custom: str = Header("default value")):
    return {"request body": user, "request custom header": x_custom}

#%---
# GET /product/{ref}
# use a sample object to test how to respond a request with an object.
# Some use cases are shown as comments.
@app_v1.get("/product/{ref}", response_model=Product,
        response_model_exclude=['supplier'],
        #response_model_include=["name", "year"],
)
async def get_product_with_ref(ref:str):
    sample_supplier_dict = {
        'id': 10001,
        'name': "sample_supplier",
        'product': ["sample prod name","sample prod name 2"],
    }
    sample_supplier = Supplier(**sample_supplier_dict)

    sample_product_dict = {
        'ref': "sample ref",
        'name': "sample prod name",
        'category': "sample prod cat",
        'supplier': sample_supplier,
        'year': 2021,
    }
    sample_product = Product(**sample_product_dict)

    return sample_product

#%---
# accepting files from a post request
# user loading files
#@app_v1.post("/user/picture")
#async def upload_user_picture(profile_picture: bytes = File(...)):
#    return {"file size": len(profile_picture)}

#%---
# send custom header to the user and accept files from a post request
# user loading files
@app_v1.post("/user/picture")
async def upload_user_picture(response: Response, profile_picture: bytes = File(...)):
    response.headers["x-file-size"] = str(len(profile_picture))
    response.set_cookie(key="cookie-api", value="test")
    return {"file size": len(profile_picture)}
