from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_session
from schemas import AlunoSchema

router = APIRouter(prefix="/aluno", tags=["aluno"])


@router.post("/", status_code=HTTPStatus.CREATED, response_model=AlunoSchema)
def create_aluno(professor: AlunoSchema, session: Session = Depends(get_session)):
    return


@router.get("/{matricula}", response_model=AlunoSchema)
def get_by_matricula_aluno(matricula: int):
    return 
