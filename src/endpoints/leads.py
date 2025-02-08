from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal, Lead
from typing import List
from models.leads_model import LeadCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1️⃣ Insertar leads
@router.post("/leads/", response_model=LeadCreate)
def create_lead(lead: LeadCreate, db: Session = Depends(get_db)):
    db_lead = Lead(name=lead.name, location=lead.location, budget=lead.budget)
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    return db_lead

# 2️⃣ Filtrar leads por ciudad o presupuesto
@router.get("/leads/", response_model=List[LeadCreate])
def get_leads(location: str = None, min_budget: float = None, db: Session = Depends(get_db)):
    query = db.query(Lead)
    
    if location:
        query = query.filter(Lead.location == location)
    if min_budget:
        query = query.filter(Lead.budget >= min_budget)
    
    leads = query.all()
    return leads

# 3️⃣ Calcular el total del presupuesto filtrado
@router.get("/leads/total-budget/")
def total_budget(location: str = None, min_budget: float = None, db: Session = Depends(get_db)):
    query = db.query(Lead)
    
    if location:
        query = query.filter(Lead.location == location)
    if min_budget:
        query = query.filter(Lead.budget >= min_budget)
    
    total = sum(lead.budget for lead in query.all())
    return {"total_budget": total}

# 4️⃣ Ordenar leads por presupuesto de mayor a menor
@router.get("/leads/sorted/", response_model=List[LeadCreate])
def get_sorted_leads(db: Session = Depends(get_db)):
    """Returns leads sorted by budget in descending order."""
    leads = db.query(Lead).order_by(Lead.budget.desc()).all()
    return leads
