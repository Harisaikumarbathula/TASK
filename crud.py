from sqlalchemy.orm import Session
import models
import schemas

# ==========================
# USER CRUD
# ==========================

def create_user(
    db: Session,
    user: schemas.UserCreate
):
    db_user = models.User(
        name=user.name,
        email=user.email
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(
        models.User
    ).all()

def get_user(
    db: Session,
    user_id: int
):
    return (
        db.query(models.User)
        .filter(
            models.User.id == user_id
        )
        .first()

    )

def update_user(
    db: Session,
    user_id: int,
    user: schemas.UserCreate
):
    db_user = (
        db.query(models.User)
        .filter(
            models.User.id == user_id
        )
        .first()
    )
    if not db_user:
        return None

    db_user.name = user.name
    db_user.email = user.email

    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(
    db: Session,
    user_id: int
):
    db_user = (
        db.query(models.User)
        .filter(
            models.User.id == user_id
        )
        .first()
    )
    if not db_user:
        return None

    db.delete(db_user)
    db.commit()
    return db_user


# ==========================
# ORDER CRUD
# ==========================

def create_order(
    db: Session,
    order: schemas.OrderCreate
):
    db_order = models.Order(
        product_name=order.product_name,
        quantity=order.quantity,
        user_id=order.user_id
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_orders(db: Session):
    return db.query(
        models.Order
    ).all()

def get_order(
    db: Session,
    order_id: int
):
    return (
        db.query(models.Order)
        .filter(
            models.Order.id == order_id
        )
        .first()
    )

def update_order(
    db: Session,
    order_id: int,
    order: schemas.OrderCreate
):
    db_order = (
        db.query(models.Order)
        .filter(
            models.Order.id == order_id
        )
        .first()
    )
    if not db_order:
        return None

    db_order.product_name = order.product_name
    db_order.quantity = order.quantity
    db_order.user_id = order.user_id

    db.commit()
    db.refresh(db_order)
    return db_order

def delete_order(
    db: Session,
    order_id: int
):
    db_order = (
        db.query(models.Order)
        .filter(
            models.Order.id == order_id
        )
        .first()
    )
    if not db_order:
        return None

    db.delete(db_order)
    db.commit()
    return db_order
