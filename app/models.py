from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import enum

Base = declarative_base()

# Enum para o estado da tarefa
class TaskStatus(enum.Enum):
    pendente = "pendente"
    em_andamento = "em andamento"
    concluida = "concluída"

# Modelo da tabela Task
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    estado = Column(Enum(TaskStatus), nullable=False, default=TaskStatus.pendente)
    data_criacao = Column(DateTime, default=datetime.utcnow)
    data_atualizacao = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
