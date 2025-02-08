from fastapi import FastAPI
from endpoints.external_data_endpoints import router as external_data_router
from config.database import init_db
from endpoints.leads import router as leads_router

app = FastAPI()

init_db()

app.include_router(external_data_router, prefix="/api")
app.include_router(leads_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Challenge!"}