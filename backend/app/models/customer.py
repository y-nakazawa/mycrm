from typing import Optional

from sqlmodel import SQLModel, Field
from app.models.base import Base


# class Customer(Base, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     name: str = Field(index=True)
#     address: str = Field(default=None)


class CustomerBase(Base):
    name: str = Field(index=True)
    address: str = Field(default=None)


class Customer(CustomerBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class CustomerCreate(CustomerBase):
    pass


class CustomerRead(CustomerBase):
    id: int


class CustomerUpdate(SQLModel):
    name: Optional[str] = None
    address: Optional[str] = None
