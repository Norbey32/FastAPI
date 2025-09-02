from sqlmodel import Session
from db import engine
from models import Customer, Transaction



session = Session(engine)
customer = Customer(
    name="Luis",
    description="Vendedor1",
    email="luis@example.com",
    age=30,
)
session.add(customer)
session.commit()

for x in range(100):
    session.add(
        Transaction(
            customer_id=customer.id,
            amount=100,
            description=f"Test number {x}",
            amount=10 * x,
        )
    )
    session.commit()