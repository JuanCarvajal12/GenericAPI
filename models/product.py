from pydantic import BaseModel
from fastapi import Query
from models.supplier import Supplier

class Product(BaseModel):
    ref: str
    name: str
    category: str
    supplier: Supplier
    year: int