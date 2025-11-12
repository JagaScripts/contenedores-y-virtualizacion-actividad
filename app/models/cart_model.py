# app/models/cart_model.py

from sqlalchemy import Column, Integer, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship
from .dec_base import DecBase

class CartItem(DecBase):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=False)
    userId = Column(Integer, ForeignKey("users.id"))
    date = Column(DateTime)
    products = Column(JSON)
    
    user = relationship("User", back_populates="carts")

def __repr__(self):
    return f"<CartItem(id={self.id}, userId={self.userId}, date={self.date}, products={self.products})>"

def to_dict(self):
    return {
        "id": self.id,
        "userId": self.userId,
        "date": self.date.isoformat() if self.date else None,
        "products": self.products
    }   

def get_id(self):
    return self.id

def get_user_id(self):
    return self.userId 

def get_date(self):
    return self.date

def get_products(self):
    return self.products

def set_user_id(self, user_id: int):
    self.userId = user_id

def set_date(self, date: DateTime):
    self.date = date

def set_products(self, products: list):
    self.products = products

def add_product(self, product: dict):
    if not self.products:
        self.products = []
    self.products.append(product)   

def remove_product(self, product_id: int):
    if self.products:
        self.products = [p for p in self.products if p.get("productId") != product_id]

def clear_products(self):
    self.products = []

    
