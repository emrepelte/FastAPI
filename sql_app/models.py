from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(120), unique=True, index=True)
    hashed_password = Column(String(120))
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(120), index=True)
    description = Column(String(120), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")


class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, index=True)
    customerId = Column(String(50))
    customerFName = Column(String(50))
    customerLName = Column(String(50))
    customerEmail = Column(String(50))
    customerPassword = Column(String(50))
    customerStreet = Column(String(50))
    customerCity = Column(String(50))
    customerState = Column(String(50))
    customerZipcode = Column(String(50))