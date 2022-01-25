from pydantic import BaseModel
from typing import List

# Supplier of the products...
class Supplier(BaseModel):
    id: int
    name: str
    products: List[str]