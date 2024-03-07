from fastapi import APIRouter, Request, Depends, HTTPException
from routes.provider.dashboard import getDashboardDetails
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/dashboard")
async def dashboard(req: Request, db: Annotated[Session, Depends(get_db)]):
    try:
        requestBody = await req.json()
        dashBoardDetails = getDashboardDetails(requestBody, db = db)
        return dashBoardDetails
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))