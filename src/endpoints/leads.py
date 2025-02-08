from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal, Lead
from typing import List
from models.leads_model import LeadCreate

router = APIRouter()

def get_db():
    """
    Dependency function to get a database session.
    Ensures that the session is properly closed after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1️⃣ Insertar leads
@router.post("/leads/", response_model=LeadCreate)
def create_lead(lead: LeadCreate, db: Session = Depends(get_db)):
    """
    Create a new lead and store it in the database.
    
    Parameters:
        lead (LeadCreate): The lead data to be stored.
        db (Session): The database session.
    
    Returns:
        LeadCreate: The newly created lead.
    """
    db_lead = Lead(name=lead.name, location=lead.location, budget=lead.budget)
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    return db_lead

@router.get("/leads/", response_model=List[LeadCreate])
def get_leads(location: str = None, min_budget: float = None, db: Session = Depends(get_db)):
    """
    Retrieve a list of leads, optionally filtered by location and minimum budget.
    
    Parameters:
        location (str, optional): Filter leads by location.
        min_budget (float, optional): Filter leads with a minimum budget.
        db (Session): The database session.
    
    Returns:
        List[LeadCreate]: A list of matching leads.
    """
    query = db.query(Lead)
    
    if location:
        query = query.filter(Lead.location == location)
    if min_budget:
        query = query.filter(Lead.budget >= min_budget)
    
    leads = query.all()
    return leads

@router.get("/leads/total-budget/")
def total_budget(location: str = None, min_budget: float = None, db: Session = Depends(get_db)):
    """
    Calculate the total budget of leads, optionally filtered by location and minimum budget.
    
    Parameters:
        location (str, optional): Filter leads by location.
        min_budget (float, optional): Filter leads with a minimum budget.
        db (Session): The database session.
    
    Returns:
        dict: A dictionary with the total budget value.
    """
    query = db.query(Lead)
    
    if location:
        query = query.filter(Lead.location == location)
    if min_budget:
        query = query.filter(Lead.budget >= min_budget)
    
    total = sum(lead.budget for lead in query.all())
    return {"total_budget": total}

@router.get("/leads/sorted/", response_model=List[LeadCreate])
def get_sorted_leads(db: Session = Depends(get_db)):
    """
    Retrieve all leads sorted by budget in descending order.
    
    Parameters:
        db (Session): The database session.
    
    Returns:
        List[LeadCreate]: A list of leads sorted by budget.
    """
    leads = db.query(Lead).order_by(Lead.budget.desc()).all()
    return leads
