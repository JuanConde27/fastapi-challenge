from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel


Base = declarative_base()

class Lead(Base):
    """
    This module defines the Lead model used for interacting with the database.
    The Lead class is a SQLAlchemy model that represents a lead with details such as:
        - id: An auto-generated unique identifier for each lead.
        - name: The name associated with the lead.
        - location: The geographical location linked to the lead.
        - budget: The financial budget associated with the lead.
    This model serves as the blueprint for the "leads" table within the database, ensuring
    that each lead record adheres to the specified schema.
    """
    __tablename__ = "leads"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    budget = Column(Numeric, nullable=False)


class LeadCreate(BaseModel):
    """
    Data model for creating a new lead.
    Attributes:
        name (str): The full name of the lead.
        location (str): The geographic location or region associated with the lead.
        budget (float): The budget allocated for the lead's project or initiative.
    """
    name: str
    location: str
    budget: float
    