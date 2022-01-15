"""
@carva

In this version file I will put the (dummy) versions of the functions
I initially created following the examples of the tutorial course I'm
following. This is for the sake of note-taking.
"""

from fastapi import FastAPI, File
from models.user import User

#%---

app_old = FastAPI(root_path='/old')

#%---

# POST /user 
# IMPORTANT: This is updated below, on advanced cases.
@app_old.post("/user") # endpoint
async def post_user(user: User):
    return {"request body": user}

#%---

# GET /product/{ref}
# this option takes the argument as a path (or an enpoint?)
# this is just the base. Below, in advance cases, is an implementation
# of what the func name indicates should do
@app_old.get("/product/{ref}")
async def get_product_with_ref(ref:str):
    return {"query path parameter": ref}

#%---
# accepting files from a post request
# user loading files
@app_old.post("/user/picture")
async def upload_user_picture(profile_picture: bytes = File(...)):
    return {"file size": len(profile_picture)}
