from pydantic import BaseModel


class OrderBase(BaseModel):
    pass


class OrderCreate(OrderBase):
    product_id: int

class OrderEdit(BaseModel):
    status: str


class Order(OrderBase):
    id: int
    orderedAt: str
    status: str
    owner_id: int
    product_id: int

    class Config:
        orm_mode = True


class CustomerBase(BaseModel):
    email: str


class CustomerCreate(CustomerBase):
    name: str
    password: str


class Customer(CustomerBase):
    id: int
    name: str
    orders: list[Order] = []
    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    product_name: str


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
