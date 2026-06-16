from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
import models
from database import engine
from database import get_db

app = FastAPI()

models.Base.metadata.create_all(
    bind=engine
)

# ==================================
# USER CRUD
# ==================================

@app.post("/users")
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    return crud.create_user(
        db,
        user
    )

@app.get("/users")
def get_users(
    db: Session = Depends(get_db)
):
    return crud.get_users(db)

@app.get("/users/{user_id}")
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = crud.get_user(
        db,
        user_id
    )
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return user

@app.put("/users/{user_id}")
def update_user(
    user_id: int,
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    updated = crud.update_user(
        db,
        user_id,
        user
    )
    if not updated:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return updated

@app.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    deleted = crud.delete_user(
        db,
        user_id
    )
    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return {
        "message": "User deleted"
    }

# ==================================
# ORDER CRUD
# ==================================

@app.post("/orders")
def create_order(
    order: schemas.OrderCreate,
    db: Session = Depends(get_db)
):
    return crud.create_order(
        db,
        order
    )

@app.get("/orders")
def get_orders(
    db: Session = Depends(get_db)
):
    return crud.get_orders(db)

@app.get("/orders/{order_id}")
def get_order(
    order_id: int,
    db: Session = Depends(get_db)
):
    order = crud.get_order(
        db,
        order_id
    )
    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )
    return order

@app.put("/orders/{order_id}")
def update_order(
    order_id: int,
    order: schemas.OrderCreate,
    db: Session = Depends(get_db)
):
    updated = crud.update_order(
        db,
        order_id,
        order
    )
    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )
    return updated

@app.delete("/orders/{order_id}")
def delete_order(
    order_id: int,
    db: Session = Depends(get_db)
):
    deleted = crud.delete_order(
        db,
        order_id
    )
    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )
    return {
        "message": "Order deleted"
    }
