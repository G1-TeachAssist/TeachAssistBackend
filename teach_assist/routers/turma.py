from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_session
from schemas import TurmaSchema

router = APIRouter(prefix="/turma", tags=["turma"])


@router.post("/", status_code=HTTPStatus.CREATED, response_model=TurmaSchema)
def create_turma(turma: TurmaSchema, session: Session = Depends(get_session)):
    return


@router.get("/{codigo_disciplina}", response_model=TurmaSchema)
def get_turmas_by_disciplina(codigo_disciplina: str):
    return 


@router.get("/{turma_id}/alunos", response_model=TurmaSchema)
def get_alunos_by_turma(turma_id: str):
    return 
