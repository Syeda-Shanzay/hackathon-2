"""
Task service module for the Todo App
Handles business logic for task operations
"""
from typing import List, Optional
from sqlmodel import Session, select
from datetime import datetime
from ..models.task import Task, TaskCreate, TaskUpdate, TaskPublic
from ..models.user import User
from ..utils.errors import TaskNotFoundException, UnauthorizedAccessException
from ..utils.logging import log_error


class TaskService:
    """Service class for task operations"""

    @staticmethod
    def get_tasks_by_user(db: Session, user_id: int, status: Optional[str] = None,
                          sort: Optional[str] = None, order: Optional[str] = None) -> List[Task]:
        """
        Get all tasks for a specific user with optional filtering and sorting
        """
        try:
            statement = select(Task).where(Task.user_id == user_id)

            # Apply status filter
            if status and status != 'all':
                if status == 'pending':
                    statement = statement.where(Task.completed == False)
                elif status == 'completed':
                    statement = statement.where(Task.completed == True)

            # Apply sorting
            if sort == 'date':
                if order == 'desc':
                    statement = statement.order_by(Task.created_at.desc())
                else:
                    statement = statement.order_by(Task.created_at.asc())
            elif sort == 'title':
                if order == 'desc':
                    statement = statement.order_by(Task.title.desc())
                else:
                    statement = statement.order_by(Task.title.asc())

            tasks = db.exec(statement).all()
            return tasks
        except Exception as e:
            log_error(e, f"TaskService.get_tasks_by_user (status={status})", user_id)
            raise

    @staticmethod
    def get_task_by_id(db: Session, task_id: int, user_id: int) -> Task:
        """
        Get a specific task by ID for a specific user
        """
        try:
            statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
            task = db.exec(statement).first()

            if not task:
                raise TaskNotFoundException(task_id)

            return task
        except TaskNotFoundException:
            raise
        except Exception as e:
            log_error(e, f"TaskService.get_task_by_id (task_id={task_id})", user_id)
            raise

    @staticmethod
    def create_task(db: Session, task_data: TaskCreate, user_id: int) -> Task:
        """
        Create a new task for a specific user
        """
        try:
            # Create task with user_id included, ensuring completed is False for new tasks
            task_dict = task_data.model_dump()
            task_dict['completed'] = False  # Override any completed value to ensure new tasks are not completed
            task_dict['user_id'] = user_id

            task = Task(**task_dict)

            db.add(task)
            db.commit()
            db.refresh(task)

            return task
        except Exception as e:
            log_error(e, "TaskService.create_task", user_id)
            db.rollback()
            raise

    @staticmethod
    def update_task(db: Session, task_id: int, task_data: TaskUpdate, user_id: int) -> Task:
        """
        Update a task for a specific user
        """
        try:
            task = TaskService.get_task_by_id(db, task_id, user_id)

            # Update fields that are provided
            update_data = task_data.model_dump(exclude_unset=True)
            for field, value in update_data.items():
                setattr(task, field, value)

            # Update the updated_at timestamp
            task.updated_at = datetime.utcnow()

            db.add(task)
            db.commit()
            db.refresh(task)

            return task
        except TaskNotFoundException:
            raise
        except Exception as e:
            log_error(e, f"TaskService.update_task (task_id={task_id})", user_id)
            db.rollback()
            raise

    @staticmethod
    def delete_task(db: Session, task_id: int, user_id: int) -> bool:
        """
        Delete a task for a specific user
        """
        try:
            task = TaskService.get_task_by_id(db, task_id, user_id)

            db.delete(task)
            db.commit()

            return True
        except TaskNotFoundException:
            raise
        except Exception as e:
            log_error(e, f"TaskService.delete_task (task_id={task_id})", user_id)
            db.rollback()
            raise

    @staticmethod
    def toggle_task_completion(db: Session, task_id: int, user_id: int) -> Task:
        """
        Toggle task completion status (between pending and completed)
        """
        try:
            task = TaskService.get_task_by_id(db, task_id, user_id)

            # Toggle the completion status
            task.completed = not task.completed
            task.updated_at = datetime.utcnow()

            db.add(task)
            db.commit()
            db.refresh(task)

            return task
        except TaskNotFoundException:
            raise
        except Exception as e:
            log_error(e, f"TaskService.toggle_task_completion (task_id={task_id})", user_id)
            db.rollback()
            raise