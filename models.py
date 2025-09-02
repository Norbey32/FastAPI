from pydantic import BaseModel
from sqlmodel import Relationship, SQLModel, Field



class CustomerBase(SQLModel):
    name: str = Field(default=None)
    name: str = Field(default=None)
    description: str | None = Field(default=None)
    email: str = Field(default=None)
    age: int = Field(default=None)

class CreateCustomer(CustomerBase):
    pass

class UpdateCustomer(CustomerBase):
    pass

class Customer(CustomerBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    transactions: list["Transaction"] = Relationship(back_populates="customer")



class TransactionBase(SQLModel):
    amount: int
    description: str

class Transaction(TransactionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    customer_id: int = Field(foreign_key="customer.id")
    customer: Customer = Relationship(back_populates="transactions")

class TransactionCreate(TransactionBase):
    customer_id: int = Field(foreign_key="customer.id")

class Invoice(BaseModel):
    id: int
    customer: Customer
    transactions: list[Transaction]
    total: int

    @property
    def amount_total(self):
        return sum(transaction.amount for transaction in self.transactions)
