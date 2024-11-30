from typing import List
from fastapi import APIRouter

from app.models import Customer

router = APIRouter()

customers = [
    {"id":1, "name": "A社", "address": "長野県長野市xxx町"},
    {"id":2, "name": "B社", "address": "長野県松本市yyy町"},
]


@router.get("/customers", response_model=List[Customer])
async def read_customers():
    return customers


@router.post("/customers", response_model=Customer)
async def create_customer(customer: Customer) :
    return customer


@router.put("/customers/{customer_id}", response_model=Customer)
async def update_customer(customer_id: int, customer: Customer):
    return customer


@router.delete("/customers/{customer_id}")
async def delete_customer(customer_id: int):
    return {"message": "Customer deleted"}
