from typing import List, Annotated
from fastapi import APIRouter, Query, HTTPException

from app.models import Customer

from app.core.db import SessionDep
from sqlmodel import select

router = APIRouter()

customers = [
    {"id":1, "name": "A社", "address": "長野県長野市xxx町"},
    {"id":2, "name": "B社", "address": "長野県松本市yyy町"},
]


@router.get("/customers", response_model=List[Customer])
async def read_customers(
        session: SessionDep,
        offset: int = 0,
        limit: Annotated[int, Query(le=100)] = 100,
    ):
    customers = session.exec(select(Customer).offset(offset).limit(limit)).all()
    return customers


@router.post("/customers", response_model=Customer)
async def create_customer(customer: Customer, session: SessionDep) :
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer


@router.put("/customers/{customer_id}", response_model=Customer)
async def update_customer(customer_id: int, customer: Customer, session: SessionDep):
    print(f"update_customer start")

    db_customer: Customer = session.get(Customer, customer_id)
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    customer_data = customer.model_dump(exclude_unset=True)
    print(f"customer_data={customer_data}")
    db_customer.sqlmodel_update(customer_data)
    session.add(db_customer)
    session.commit()
    session.refresh(db_customer)

    print(f"update_customer end")
    return db_customer


@router.delete("/customers/{customer_id}")
async def delete_customer(customer_id: int, session: SessionDep):
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    session.delete(customer)
    session.commit()
    return {"ok": True}
