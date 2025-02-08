from pydantic import BaseModel

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