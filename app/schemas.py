from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class TaskStatus(str, Enum):
    pendente = "pendente"
    em_andamento = "em andamento"
    concluida = "concluída"


class TaskBase(BaseModel):
    titulo: str
    descricao: str | None = None
    estado: TaskStatus


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    pass


class TaskResponse(TaskBase):
    id: int
    data_criacao: datetime
    data_atualizacao: datetime

    class Config:
        orm_mode = True
