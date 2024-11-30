from fastapi import APIRouter

from app.api.routes import hello,customer

api_router = APIRouter()
#api_router.include_router(hello.router, tags=["hello"])
api_router.include_router(customer.router, tags=["customer"])

