from fastapi import FastAPI

app = FastAPI()

@app.get("/in/{name}")
def greet(name: str):
    return f"Hello {name}!"


@app.get("/{org}/student/{name}")
def greet(org: str, name: str):
    return f"Hello {name} from {org}!"



@app.get("/items/{item_id}")
# the above line describes the path operation decorator. item_id is a path parameter.
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    # the above line describes the path operation function. q is a query parameter and short is a query parameter with a default value.
    item = {"item_id": item_id}

    if q:
        item.update({"q": q})
        #
    if not short:
        #
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item