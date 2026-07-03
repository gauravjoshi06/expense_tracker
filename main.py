"""
main.py

Main FastAPI application for Expense Tracker.
"""

from fastapi import FastAPI, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from models import Transaction

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(title="Expense Tracker")

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates folder
templates = Jinja2Templates(directory="templates")


# ==============================
# Home Page
# ==============================
@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):

    # Get all transactions
    transactions = db.query(Transaction).all()

    # Calculate totals
    income = sum(
        transaction.amount
        for transaction in transactions
        if transaction.type.lower() == "income"
    )

    expense = sum(
        transaction.amount
        for transaction in transactions
        if transaction.type.lower() == "expense"
    )

    balance = income - expense

    # Render Home Page
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "transactions": transactions,
            "income": income,
            "expense": expense,
            "balance": balance,
        },
    )


# ==============================
# Add Transaction
# ==============================
@app.post("/add")
def add_transaction(
    title: str = Form(...),
    amount: float = Form(...),
    category: str = Form(...),
    type: str = Form(...),
    db: Session = Depends(get_db),
):

    new_transaction = Transaction(
        title=title,
        amount=amount,
        category=category,
        type=type,
    )

    db.add(new_transaction)
    db.commit()

    return RedirectResponse(url="/", status_code=303)


# ==============================
# Delete Transaction
# ==============================
@app.get("/delete/{id}")
def delete_transaction(id: int, db: Session = Depends(get_db)):

    transaction = db.query(Transaction).filter(
        Transaction.id == id
    ).first()

    if transaction:
        db.delete(transaction)
        db.commit()

    return RedirectResponse(url="/", status_code=303)


# ==============================
# Edit Page
# ==============================
@app.get("/edit/{id}", response_class=HTMLResponse)
def edit_page(
    id: int,
    request: Request,
    db: Session = Depends(get_db),
):

    transaction = db.query(Transaction).filter(
        Transaction.id == id
    ).first()

    if transaction is None:
        return RedirectResponse(url="/", status_code=303)

    return templates.TemplateResponse(
        request=request,
        name="edit.html",
        context={
            "transaction": transaction,
        },
    )


# ==============================
# Update Transaction
# ==============================
@app.post("/update/{id}")
def update_transaction(
    id: int,
    title: str = Form(...),
    amount: float = Form(...),
    category: str = Form(...),
    type: str = Form(...),
    db: Session = Depends(get_db),
):

    transaction = db.query(Transaction).filter(
        Transaction.id == id
    ).first()

    if transaction:
        transaction.title = title
        transaction.amount = amount
        transaction.category = category
        transaction.type = type

        db.commit()

    return RedirectResponse(url="/", status_code=303)