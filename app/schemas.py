from pydantic import BaseModel
from datetime import datetime

class TaskBase(BaseModel):
    nome: str

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class TaskOut(TaskBase):
    id: int
    data_criacao: datetime
    data_atualizacao: datetime

    class Config:
        orm_mode = True
