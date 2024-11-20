from fastapi import FastAPI
from .models import Item

# Create the FastAPI instance
app = FastAPI()

# Define a route
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

@app.post("/items/")
def create_item(item: Item):
    return {
        "name": item.name,
        "price": item.price,
        "tax": item.tax,
        "description": item.description,
    }