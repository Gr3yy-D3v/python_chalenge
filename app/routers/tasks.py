from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import TaskCreate, TaskUpdate, TaskOut
from app.crud import create_task, get_task, get_tasks, update_task, delete_task
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TaskOut)
def create(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task)

@router.get("/", response_model=list[TaskOut])
def list_all(db: Session = Depends(get_db)):
    return get_tasks(db)

@router.get("/{task_id}", response_model=TaskOut)
def read(task_id: int, db: Session = Depends(get_db)):
    task = get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=TaskOut)
def update(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    updated_task = update_task(db, task_id, task)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@router.delete("/{task_id}")
def delete(task_id: int, db: Session = Depends(get_db)):
    deleted_task = delete_task(db, task_id)
    if not deleted_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}
