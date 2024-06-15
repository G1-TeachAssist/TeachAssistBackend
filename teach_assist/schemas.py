from typing import List
from pydantic import BaseModel, EmailStr


class ProfessorSchema(BaseModel):
    nome: str
    email: str
    senha: str
    papel: str


class ProfessorPublic(BaseModel):
    id: int
    username: str
    email: EmailStr


class AlunoSchema(BaseModel):
    nome: str
    matricula: str


class DisciplinaSchema(BaseModel):
    nome: str
    codigo: str


class TurmaSchema(BaseModel):
    ano: str
    semestre: str
    disciplina_id: int
    professor_id: int
    alunos: List[int]


class NotaSchema(BaseModel):
    aluno_id: int
    turma_id: int
    nota: float
