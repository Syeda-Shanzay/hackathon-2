"""
Task API endpoints for the Todo App
Handles all task-related API operations
"""
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from ...models.task import Task, TaskCreate, TaskUpdate, TaskPublic
from ...models.user import User
from ..deps import get_current_active_user, get_db_session  # Fixed path - deps is in parent directory (api/)
from ...services.task_service import TaskService
from ...utils.errors import TaskNotFoundException, UnauthorizedAccessException

router = APIRouter()


@router.get("/", response_model=List[Task])
def get_tasks(
    status_filter: Optional[str] = None,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session)
):
    """
    Get all tasks for the authenticated user with optional filtering and sorting
    """
    tasks = TaskService.get_tasks_by_user(
        db=db,
        user_id=current_user.id,
        status=status_filter,
        sort=sort,
        order=order
    )
    return tasks


@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(
    task_create: TaskCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session)
):
    """
    Create a new task for the authenticated user
    """
    task = TaskService.create_task(
        db=db,
        task_data=task_create,
        user_id=current_user.id
    )
    return task


@router.get("/{task_id}", response_model=Task)
def get_task(
    task_id: int,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session)
):
    """
    Get a specific task by ID for the authenticated user
    """
    task = TaskService.get_task_by_id(
        db=db,
        task_id=task_id,
        user_id=current_user.id
    )
    return task


@router.put("/{task_id}", response_model=Task)
def update_task(
    task_id: int,
    task_update: TaskUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session)
):
    """
    Update a specific task by ID for the authenticated user
    """
    task = TaskService.update_task(
        db=db,
        task_id=task_id,
        task_data=task_update,
        user_id=current_user.id
    )
    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session)
):
    """
    Delete a specific task by ID for the authenticated user
    """
    TaskService.delete_task(
        db=db,
        task_id=task_id,
        user_id=current_user.id
    )
    return {"message": "Task deleted successfully"}


@router.patch("/{task_id}/complete", response_model=Task)
def complete_task(
    task_id: int,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session)
):
    """
    Mark a specific task as complete for the authenticated user
    """
    task = TaskService.toggle_task_completion(
        db=db,
        task_id=task_id,
        user_id=current_user.id
    )
    return task


@router.patch("/{task_id}/reopen", response_model=Task)
def reopen_task(
    task_id: int,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db_session)
):
    """
    Reopen a specific completed task for the authenticated user
    """
    task = TaskService.toggle_task_completion(
        db=db,
        task_id=task_id,
        user_id=current_user.id
    )
    return task