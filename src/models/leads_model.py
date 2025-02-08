from pydantic import BaseModel

class LeadCreate(BaseModel):
    name: str
    location: str
    budget: float