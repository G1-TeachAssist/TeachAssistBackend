from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_session
from schemas import NotaSchema

router = APIRouter(prefix="/notas", tags=["nota"])


@router.post("/", status_code=HTTPStatus.CREATED, response_model=NotaSchema)
def create_nota(nota: NotaSchema, session: Session = Depends(get_session)):
    return


@router.get("/{aluno_id}", response_model=NotaSchema)
def get_notas_by_aluno(aluno_id: int):
    return


@router.get("/{turma_id}/alunos", response_model=NotaSchema)
def get_notas_by_turma(turma_id: int):
    return


@router.get("/{turma_id}/{aluno_id}", response_model=NotaSchema)
def get_notas_by_turma_and_aluno(aluno_id: int, turma_id: int):
    return
