from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_session
from models import Professor
from schemas import ProfessorSchema, ProfessorPublic

router = APIRouter(prefix="/professor", tags=["professor"])


@router.post("/", status_code=HTTPStatus.CREATED, response_model=ProfessorPublic)
def create_professor(professor: ProfessorSchema, session: Session = Depends(get_session)):
    db_professor = session.scalar(
        select(Professor).where((Professor.email == professor.email))
    )

    if db_professor:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Email already exists",
        )

    db_professor = Professor(
        nome=user.nome,
        email=user.email,
        senha=user.senha,
        papel=user.papel
    )

    session.add(db_professor)
    session.commit()
    session.refresh(db_professor)

    return db_professor


@router.get("/{professor_id}", response_model=ProfessorPublic)
def get_by_id_professor(professor_id: int):
    return 


@router.get("/{professor_email}", response_model=ProfessorPublic)
def get_by_email_professor(professor_email: str):
    return 
