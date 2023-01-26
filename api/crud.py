from sqlalchemy.orm import Session
from datetime import datetime

import models
import schemas
import auth


def get_customer(db: Session, user_id: int):
    return db.query(models.Customer).filter(models.Customer.id == user_id).first()


def get_customer_by_email(db: Session, email: str):
    return db.query(models.Customer).filter(models.Customer.email == email).first()


def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Customer).offset(skip).limit(limit).all()


def create_customer(db: Session, customer: schemas.CustomerCreate):
    hashed_password = auth.get_password_hash(customer.password)
    db_user = models.Customer(email=customer.email, password=hashed_password, name=customer.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Order).offset(skip).limit(limit).all()


def create_customer_order(db: Session, item: schemas.OrderCreate, user_id: int):
    db_item = models.Order(**item.dict(), owner_id=user_id, orderedAt=datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S"), status="Processing")
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def edit_order(db: Session, item = schemas.OrderEdit, order_id = int):
    db_item = db.query(models.Order).filter(models.Order.id == order_id).first()
    db_item.status = item.status
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_order(db: Session, order_id = int):
    db_item = db.query(models.Order).filter(models.Order.id == order_id).first()
    db.delete(db_item)
    db.commit()
    return {"detail": "The order has been deleted"}


def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def get_product_by_name(db: Session, product_name: str):
    return db.query(models.Customer).filter(models.Product.product_name == product_name).first()


def create_product(db: Session, item: schemas.ProductCreate):
    db_item = models.Product(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
