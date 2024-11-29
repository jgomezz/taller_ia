from pydantic import BaseModel

# Python type annotations.
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None