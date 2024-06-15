from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, registry, relationship

table_registry = registry()


@table_registry.mapped_as_dataclass
class Aluno():
    __tablename__ = "alunos"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome = Mapped[str]
    matricula = Mapped[str]


@table_registry.mapped_as_dataclass
class Disciplina():
    __tablename__ = "disciplinas"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome = Mapped[str]
    codigo = Mapped[str]


@table_registry.mapped_as_dataclass
class Nota():
    __tablename__ = "notas"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    notas = Mapped[float]

    aluno_id: Mapped[int] = mapped_column(ForeignKey("turmas.id"))
    turma_id: Mapped[int] = mapped_column(ForeignKey("turmas.id"))

    aluno: Mapped['Aluno'] = relationship("Aluno", back_populates="notas")
    turma: Mapped['Turma'] = relationship("Turma", back_populates="notas")


@table_registry.mapped_as_dataclass
class Professor():
    __tablename__ = "professores"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str]
    email: Mapped[str]
    senha: Mapped[str]
    papel: Mapped[str]


@table_registry.mapped_as_dataclass
class Turma():
    __tablename__ = "turmas"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    ano = Mapped[int]
    semestre = Mapped[str]

    disciplina_id: Mapped[int] = mapped_column(ForeignKey("disciplina.id"))
    professor_id: Mapped[int] = mapped_column(ForeignKey("professor.id"))
