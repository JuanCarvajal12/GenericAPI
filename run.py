
# when deving on VSCode in my machine, change interpreter with
# (Ctrl+Shift+P) | >Python:Select Interpreter | 'fastapidev' conda

# run with
#       uvicorn run:app --reload --port 3000
# --reload enables auto-refreshing when updating code.

# In this examples for each of the requests I'm just printing the
# parameters, at first. I'm aware in the middle I can do whatever
# I want with python as long as I return an appropriate result.


#%---
from models.user import User
from models.product import Product
from models.supplier import Supplier
from fastapi import FastAPI

# This `Body` function allows a variable to be treated as an object,
# which enables it to be passed in a POST request as a JSON object.
# The parameter "embed" is neccesary under reasons explicit on "embed".
from fastapi import Body


app = FastAPI()


# POST /user
@app.post("/user") # endpoint
async def post_user(user: User):

    return {"request body": user}

# Two different types of GET requests

## GET /user?password
### this version takes the argument as a query parameter
@app.get("/user")
async def get_user_validation(password:str):
    return {"query parameter": password}

## GET /product/{ref}
### this option takes the argument as a path (or an enpoint)
@app.get("/product/{ref}")
async def get_product_with_ref(ref:str):
    return {"query path parameter": ref}

# A combination of these two types into one path+query

## GET /supplier/{id}/product?year&category&order
## This would mean I want to query the products that fall in some 
## category and year, from a supplier with a specific id, in a certain
## order.
@app.get("/supplier/{id}/product")
async def get_suppliers_products(id: int, year:int, category:str, order: str = 'asc'):
    return {"query parameters": str(id)+' '+str(year)+' '+category+' '+order}

# PATCH /supplier/name
@app.patch("/supplier/name")
async def patch_supplier_name(name: str = Body(...,embed=True)):
    # we set embed=True so that I can pass the parameter 'name' as a JSON
    return {"name in body": name}

# POST /user/supplier
# This takes both the supplier and the product as parameters for the POST request.
# This takes an additional dummy parameter to show the incorporation of a variable
# in the request.
@app.post("/user/supplier")
async def post_user_and_author(user: User, supplier: Supplier, dummy_param:str = Body(...,embed=True)):
    return {'user': user, 'supplier': supplier, 'dummy_param': dummy_param}