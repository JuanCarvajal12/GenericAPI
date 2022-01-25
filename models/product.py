from pydantic import BaseModel, Field
from fastapi import Query
from models.supplier import Supplier
from utils.const import *

class Product(BaseModel):
    ref: str = Field('sting', description=REF_DESCRIPTION)
    name: str
    category: str
    supplier: Supplier
    year: int = Field(2000, gt=1990, lt=2022)