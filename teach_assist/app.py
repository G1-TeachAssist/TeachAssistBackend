from http import HTTPStatus

from fastapi import FastAPI

from routers import aluno, disciplina, nota, professor, turma


app = FastAPI()

app.include_router(aluno.router)
app.include_router(disciplina.router)
app.include_router(nota.router)
app.include_router(professor.router)
app.include_router(turma.router)


@app.get("/ping", status_code=HTTPStatus.OK)
async def ping():
    return "pong"
