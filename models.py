from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )
    name = Column(String)
    email = Column(
        String,
        unique=True
    )

    orders = relationship(
        "Order",
        back_populates="user",
        cascade="all, delete"
    )

class Order(Base):
    __tablename__ = "orders"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )
    product_name = Column(String)
    quantity = Column(Integer)
    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE")
    )

    user = relationship(
        "User",
        back_populates="orders"
    )
