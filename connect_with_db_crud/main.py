from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from crud import create_todo, update_todo, delete_todo, get_todos
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/todos/")
def create_todo_api(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    todos = create_todo(db=db,todo=todo)
    return todos

@app.put("/todos/")
def update_todo_api(todo: schemas.TodoUpdate, db: Session = Depends(get_db)):
    return update_todo(db=db,todo=todo)
    # updated_todos = update_todo(db=db,todo=todo)
    # return updated_todos

@app.delete("/todos/")
def delete_todo_api(todo: schemas.TodoDelete, db: Session = Depends(get_db)):
    delete_todos = delete_todo(db=db,todo=todo)
    return delete_todos

@app.get("/todos/", response_model=list[schemas.TodoCreate])
def get_todo_api(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
     all_todos = get_todos(db, skip=skip, limit=limit)
     return all_todos


# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @app.get("/items/", response_model=list[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items