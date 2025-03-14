from fastapi import FastAPI, HTTPException, status
from models import CustomerCreate, Transaction, Invoice, Customer, CustomerUpdate
from db import SessionDep, create_all_tables
from sqlmodel import select

app = FastAPI(lifespan=create_all_tables)

# Definir una base de datos en memoria para clientes
db_customers: list[Customer] = []

@app.post('/customers', response_model=Customer)
async def create_customer(customer_data: CustomerCreate, session: SessionDep):
    customer = Customer(**customer_data.model_dump())  # Crear un nuevo objeto Customer
    session.add(customer)
    session.commit()
    session.refresh(customer)
    # customer.id = len(db_customers) + 1  # Generar un ID único
    # db_customers.append(customer)  # Agregar a la lista de clientes
    return customer

# @app.get("/customers/{customer_id}", response_model=Customer)
# async def read_customer(customer_id : int, session:SessionDep):
#     customer_db = session.get(Customer, customer_id)
#     if not customer_db:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="customer doesn't exits ")
#     return customer_db



# @app.patch("/customers/{customer_id}", response_model=Customer, status_code=status.HTTP_201_CREATED)
# async def update_customer(customer_id : int,customer_data: CustomerUpdate ,session:SessionDep):
#     customer_db = session.get(Customer, customer_id)
#     if not customer_db:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="customer doesn't exits ")
#     customer_data_dict = customer_data.model_dump(exclude_unset=True)
#     customer_db.sqlmodel_update(customer_data_dict)
#     session.add(customer_db)
#     session.commit()
#     session.refresh(customer_db)
#     return customer_db


# @app.delete("/customers/{customer_id}")
# async def delete_customer(customer_id : int, session:SessionDep):
    
#     customer_db = session.get(Customer, customer_id)
#     if not customer_db:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="customer doesn't exits ")
#     session.delete(customer_db)
#     session.commit()
#     return {"detail":"ok"}


# @app.get("/customers", response_model=list[Customer])
# async def list_customers( session: SessionDep):
    
#     return session.exec(select(Customer)).all()

# @app.get("/customer/{id}", response_model=Customer)
# async def customer(id: int):
#     for i in db_customers:
#         if i.id == id:
#             return i

@app.post('/transactions')
async def create_transaction(transaction_data: Transaction):
    return transaction_data

@app.post('/invoice')
async def create_invoice(invoice_data: Invoice):
    return invoice_data

