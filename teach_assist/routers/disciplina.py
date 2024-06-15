from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_session
from schemas import DisciplinaSchema

router = APIRouter(prefix="/disciplina", tags=["disciplina"])


@router.post("/", status_code=HTTPStatus.CREATED, response_model=DisciplinaSchema)
def create_disciplina(disciplina: DisciplinaSchema, session: Session = Depends(get_session)):
    return


@router.get("/{codigo}", response_model=DisciplinaSchema)
def get_disciplina_by_codigo(codigo: str):
    return 
