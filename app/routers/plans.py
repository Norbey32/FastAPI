from fastapi import APIRouter
from sqlmodel import select
from models import Plan
from db import SessionDep
from fastapi import status


router = APIRouter()


@router.post("/plans", status_code=status.HTTP_201_CREATED, tags=["plans"])
def create_plan(plan_data: Plan, session: SessionDep):
    plan_db = Plan.model_validate(plan_data.model_dump())
    session.add(plan_db)
    session.commit()
    session.refresh(plan_db)
    return plan_db


@router.get("/plans", response_model=list[Plan], tags=["plans"])
def list_plans(session: SessionDep):
    plans = session.exec(select(Plan)).all()
    return plans





