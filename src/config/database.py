from sqlalchemy import create_engine, Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

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


def init_db():
    Base.metadata.create_all(bind=engine)
