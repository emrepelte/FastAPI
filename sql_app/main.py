from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .database import SessionLocal, engine

import pandas as pd
import os

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
async def startup_event():
    db = SessionLocal()
    df = pd.read_csv('https://raw.githubusercontent.com/erkansirin78/datasets/master/retail_db/customers.csv')
    df = df.head(10)
    for index, row in df.iterrows():
        customer = Customer(
            customerId=row['customerId'],
            customerFName=row['customerFName'],
            customerLName=row['customerLName'],
            customerEmail=row['customerEmail'],
            customerPassword=row['customerPassword'],
            customerStreet=row['customerStreet'],
            customerCity=row['customerCity'],
            customerState=row['customerState'],
            customerZipcode=row['customerZipcode'],
        )
        db.add(customer)
    db.commit()



@app.put("/update_customer/{customerId}")
async def update_customer(customerId: int, customerLName: str):
    db = SessionLocal()
    customer = db.query(Customer).filter(Customer.id == customerId).first()
    if customer:
        customer.customerLName = customerLName
        db.commit()
        return {"message": "Customer updated successfully"}
    else:
        return {"message": "Customer not found"}