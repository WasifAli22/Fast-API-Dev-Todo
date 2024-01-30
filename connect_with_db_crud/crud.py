from sqlalchemy.orm import Session
import models, schemas

def get_todo(db: Session, id: int):
    return db.query(models.Todo).filter(models.Todo.id == id).first()

def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todo).offset(skip).limit(limit).all()

def create_todo(db: Session, todo: schemas.TodoCreate):
     db_todo = models.Todo(text = todo.text)
     db.add(db_todo)
     db.commit()
     db.refresh(db_todo)
     return "Todo has been created...😍"

def update_todo(db: Session, todo: schemas.TodoUpdate):
     db_todo = db.query(models.Todo).filter(models.Todo.id == todo.id).first()
     db_todo.text = todo.text
     db.add(db_todo)
     db.commit()
     db.refresh(db_todo)
     return "Todo has been Updated...😍"

def delete_todo(db: Session, todo: schemas.TodoDelete):
     db_todo = db.query(models.Todo).filter(models.Todo.id == todo.id).first()
     db.delete(db_todo)
     db.commit()
     return "Todo has been Deleted...😍"

# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item