from fastapi import FastAPI

app = FastAPI()

@app.get("/in/{name}")
def greet(name: str):
    return f"Hello {name}!"


@app.get("/{org}/student/{name}")
def greet(org: str, name: str):
    return f"Hello {name} from {org}!"