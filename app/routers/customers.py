from fastapi import FastAPI, HTTPException, status, APIRouter
from models import CustomerCreate, Customer, CustomerUpdate
from db import SessionDep

from sqlmodel import select


router = APIRouter()




@router.post('/customers', response_model=Customer, tags=['customers'])
async def create_customer(customer_data: CustomerCreate, session: SessionDep):
    customer = Customer(**customer_data.model_dump())  # Crear un nuevo objeto Customer
    session.add(customer)
    session.commit()
    session.refresh(customer)
    # customer.id = len(db_customers) + 1  # Generar un ID único
    # db_customers.append(customer)  # Agregar a la lista de clientes
    return customer

@router.get("/customers/{customer_id}", response_model=Customer,tags=['customers'])
async def read_customer(customer_id : int, session:SessionDep):
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="customer doesn't exits ")
    return customer_db



@router.patch("/customers/{customer_id}", response_model=Customer, status_code=status.HTTP_201_CREATED,tags=['customers'])
async def update_customer(customer_id : int,customer_data: CustomerUpdate ,session:SessionDep):
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="customer doesn't exits ")
    customer_data_dict = customer_data.model_dump(exclude_unset=True)
    customer_db.sqlmodel_update(customer_data_dict)
    session.add(customer_db)
    session.commit()
    session.refresh(customer_db)
    return customer_db


@router.delete("/customers/{customer_id}",tags=['customers'])
async def delete_customer(customer_id : int, session:SessionDep):
    
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="customer doesn't exits ")
    session.delete(customer_db)
    session.commit()
    return {"detail":"ok"}


@router.get("/customers", response_model=list[Customer],tags=['customers'])
async def list_customers( session: SessionDep):
    
    return session.exec(select(Customer)).all()


