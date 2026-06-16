from pydantic import BaseModel

# --------------------
# USER
# --------------------
class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(UserCreate):
    id: int

    class Config:
        from_attributes = True

# --------------------
# ORDER
# --------------------
class OrderCreate(BaseModel):
    product_name: str
    quantity: int
    user_id: int

class OrderResponse(OrderCreate):
    id: int
    name: str | None = None
    email: str | None = None

    class Config:
        from_attributes = True
