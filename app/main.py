from fastapi import FastAPI
from models import Transaction, Invoice, Customer
from db import create_all_tables
from sqlmodel import select
from .routers import customers

app = FastAPI(lifespan=create_all_tables)
app.include_router(customers.router)
# Definir una base de datos en memoria para clientes
db_customers: list[Customer] = []

@app.post('/transactions')
async def create_transaction(transaction_data: Transaction):
    return transaction_data

@app.post('/invoice')
async def create_invoice(invoice_data: Invoice):
    return invoice_data

