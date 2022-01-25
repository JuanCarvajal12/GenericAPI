"""
@carva

when deving on VSCode in my machine, change interpreter with
(Ctrl+Shift+P) | >Python:Select Interpreter | 'fastapidev' conda

version 2. Further learning about FastAPI. Integrating with the database.
"""

#%---
from http.client import HTTPException
from models.user import User
from models.product import Product
from models.supplier import Supplier
from fastapi import Header, File, Body, APIRouter
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from utils.const import USER_SUMMARY
from utils.db_functions import (db_get_supplier_with_name, db_insert_personel, 
    db_check_personel, db_get_product_with_ref, db_get_supplier_with_id,
    db_patch_supplier_name)
from starlette.responses import Response
from utils.helper_functions import upload_image_to_server

#%---
app_v2 = APIRouter()

#%---
# POST /user
# IMPORTANT: In python i wrote 'x_custom', but in the request I use 'x-custom'.
## ADDED FUNCTIONALITY: Now this function requires authentication and authori-
## zation. In the header of the request, should appear the Authorization entry
## with value "Bearer <token>". The token is generated with POST -> /v1/token.
@app_v2.post("/user", status_code=HTTP_201_CREATED, tags=["User"],
summary=USER_SUMMARY) # endpoint
async def post_user(user: User):
    await db_insert_personel(user)
    return {"result": "personel is created"}


#%---
## POST /login
@app_v2.post("/login", tags=['User']) # /user?password=*****
async def get_user_validation(username: str = Body(...), password: str = Body(...)):
    result = await db_check_personel(username, password)
    return {"IS_VALID": result}

#%---
# GET /product/{ref}
@app_v2.get("/product/{ref}", response_model=Product,
        #response_model_exclude=['supplier'],
        #response_model_include=["name", "year"],
        tags=['Product']
)
async def get_product_with_ref(ref:str):

    product = await db_get_product_with_ref(ref)
    supplier_name = product['supplier']
    supplier = await db_get_supplier_with_name(supplier_name)
    supplier_instance = Supplier(**supplier)
    product['supplier'] = supplier_instance
    result_product = Product(**product)
    return result_product

#%---
## GET /supplier/{id}/product?order
## Query the products of the supplier with a certain id, in a certain
## order.
@app_v2.get("/supplier/{id}/product", tags=["Product", "Supplier"])
async def get_suppliers_products(id: int, order: str = 'asc'):
    supplier = await db_get_supplier_with_id(id)
    if supplier is not None:
        products = supplier["products"]
        if order == 'asc':
            products = sorted(products)
        elif order == 'desc':
            products = sorted(products, reverse=True)
        else:
            raise HTTPException(HTTP_400_BAD_REQUEST)
        return {"products": products}
    else:
        return {"error": "no author with corresponding id"}

#%---
# PATCH /supplier/{id}/name
@app_v2.patch("/supplier/{id}/name", tags=["Supplier"])
async def patch_supplier_name(id: int,  name: str = Body(...,embed=True)):
    await db_patch_supplier_name(id, name)
    return {"result": "name is updated"}

#%---
# POST /user/picture
@app_v2.post("/user/picture", tags=['Supplier'])
async def upload_user_picture(response: Response, profile_picture: bytes = File(...)):
    await upload_image_to_server(profile_picture)
    return {"file size": len(profile_picture)}

