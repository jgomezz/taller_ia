from fastapi import FastAPI
from .models import Item

# Create the FastAPI instance
app = FastAPI()

# Define a route
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/items/")
def read_items(id: int = 1, name: str = "Jaime"):
    return {"id": id, "name": name}

@app.post("/items/")
def create_item(item: Item):
    return item

    return {
        "name": item.name,
        "price": item.price,
        "tax": item.tax,
        "description": item.description,
    }

import asyncio

@app.get("/async")
async def get_async():
    await asyncio.sleep(1)
    return {"message": "This was async"}

