from pydantic import BaseModel, Field
from fastapi import Query
from models.supplier import Supplier
from utils.const import *

class Product(BaseModel):
    ref: str = Field('sting', description=REF_DESCRIPTION)
    name: str
    category: str
    supplier: Supplier
    year: int = Field(2000, lt=1990, gt=2022)