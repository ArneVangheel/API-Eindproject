from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

import crud
import models
import schemas
import auth
import os
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

#"sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost/",
    "http://localhost:8080/",
    "http://localhost:63342",
    "https://localhost.tiangolo.com/",
    "http://127.0.0.1:5500/",
    "http://127.0.0.1:8080",
    "https://delightful-kashata-80ca8b.netlify.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/register", response_model=schemas.Customer)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_user = crud.get_customer_by_email(db, email=customer.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_customer(db=db, customer=customer)


@app.get("/customers", response_model=list[schemas.Customer])
def get_customer(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    users = crud.get_customers(db, skip=skip, limit=limit)
    return users


@app.get("/customers/{user_id}", response_model=schemas.Customer)
def get_customer_by_id(user_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_user = crud.get_customer(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_user


@app.post("/customers/{customer_id}/orders/", response_model=schemas.Order)
def create_order_for_customer(customer_id: int, item: schemas.OrderCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    #controleer of het product_id bestaat, dus dat er een product op dit id is.
    db_user = crud.get_product(db, product_id=item.product_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="There is no Product registered")

    return crud.create_customer_order(db=db, item=item, user_id=customer_id)


@app.get("/orders", response_model=list[schemas.Order])
def get_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_orders(db, skip=skip, limit=limit)
    return items


@app.put("/orders/{order_id}", response_model=schemas.Order)
def edit_order(order_id: int, item: schemas.OrderEdit, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    #Controleer of er een order op dit id staat
    db_order = crud.get_order(db, order_id=order_id)
    if not db_order:
        raise HTTPException(status_code=400, detail="There is no Order registered")
    db_item = crud.edit_order(db, item, order_id=order_id)
    return db_item


@app.delete("/orders/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    #Controleer of er een order op dit id staat
    db_order = crud.get_order(db, order_id=order_id)
    if not db_order:
        raise HTTPException(status_code=400, detail="There is no Order registered")
    #Zoja, verwijder de order
    items = crud.delete_order(db, order_id=order_id)
    if not items:
        raise HTTPException(status_code=400, detail="The order has been deleted")
    return items

@app.get("/products", response_model=list[schemas.Product])
def get_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products

@app.post("/products", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    #controleer of er al een product op die naam staat, als dit het geval is geeft dan een exception status.
    db_product = crud.get_product_by_name(db, product_name=product.product_name)
    if db_product:
        raise HTTPException(status_code=400, detail="This Product is already registered")
    print(product)
    return crud.create_product(db=db, item=product)


@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me", response_model=schemas.Customer)
def read_users_me(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    current_user = auth.get_current_customer(db, token)
    return current_user
