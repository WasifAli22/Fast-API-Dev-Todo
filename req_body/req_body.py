from fastapi import FastAPI
from models import Item

app = FastAPI()

@app.post("/items")
async def create_item(item: Item):
    return item.name

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}
