from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List, Optional
from sqlmodel import Session

from ...database.database import get_session
from ...models.task import TaskPublic, TaskCreate, TaskUpdate
from ...services.task_service import TaskService
from ...api.deps import get_current_user
from ...models.user import User
from ...utils.errors import UnauthorizedAccessException


router = APIRouter()


@router.get("/{user_id}/tasks", response_model=List[TaskPublic])
async def get_tasks(
    user_id: int,
    status_filter: Optional[str] = Query(None, alias="status", description="Filter tasks by status: all, pending, completed"),
    sort: Optional[str] = Query(None, description="Sort by: date, title"),
    order: Optional[str] = Query(None, description="Sort order: asc, desc"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=0, le=100),
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Retrieve all tasks for a user with optional filtering and pagination.

    Args:
        user_id: ID of the user whose tasks to retrieve
        status_filter: Filter tasks by status ('all', 'pending', 'completed')
        sort: Sort by ('date', 'title')
        order: Sort order ('asc', 'desc')
        skip: Number of records to skip for pagination
        limit: Maximum number of records to return
        current_user: Currently authenticated user
        session: Database session

    Returns:
        List of tasks for the user

    Raises:
        HTTPException: If user tries to access another user's tasks
    """
    # Verify that the requested user_id matches the authenticated user's ID
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only access your own tasks"
        )

    try:
        tasks = TaskService.get_tasks_by_user(
            db=session,
            user_id=user_id,
            status=status_filter,
            sort=sort,
            order=order
        )

        # Return only the tasks that belong to the current user
        return [task for task in tasks if task.user_id == user_id]

    except UnauthorizedAccessException:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to access these tasks"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while retrieving tasks: {str(e)}"
        )


@router.post("/{user_id}/tasks", response_model=TaskPublic, status_code=status.HTTP_201_CREATED)
async def create_task(
    user_id: int,
    task_create: TaskCreate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Create a new task for the authenticated user.

    Args:
        user_id: ID of the user creating the task (should match authenticated user)
        task_create: Task creation data
        current_user: Currently authenticated user
        session: Database session

    Returns:
        Created task

    Raises:
        HTTPException: If user tries to create a task for another user
    """
    # Verify that the requested user_id matches the authenticated user's ID
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only create tasks for yourself"
        )

    try:
        created_task = TaskService.create_task(
            db=session,
            task_data=task_create,
            user_id=user_id
        )

        return created_task

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while creating the task: {str(e)}"
        )


@router.get("/{user_id}/tasks/{task_id}", response_model=TaskPublic)
async def get_task(
    user_id: int,
    task_id: int,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Retrieve a specific task by ID for the authenticated user.

    Args:
        user_id: ID of the user requesting the task (should match authenticated user)
        task_id: ID of the task to retrieve
        current_user: Currently authenticated user
        session: Database session

    Returns:
        The requested task

    Raises:
        HTTPException: If user tries to access another user's task or task doesn't exist
    """
    # Verify that the requested user_id matches the authenticated user's ID
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only access your own tasks"
        )

    try:
        task = TaskService.get_task_by_id(
            db=session,
            task_id=task_id,
            user_id=user_id
        )

        return task

    except Exception as e:
        if "not found" in str(e).lower():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Task with ID {task_id} not found"
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An error occurred while retrieving the task: {str(e)}"
            )


@router.put("/{user_id}/tasks/{task_id}", response_model=TaskPublic)
async def update_task(
    user_id: int,
    task_id: int,
    task_update: TaskUpdate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Update a specific task for the authenticated user.

    Args:
        user_id: ID of the user updating the task (should match authenticated user)
        task_id: ID of the task to update
        task_update: Updated task data
        current_user: Currently authenticated user
        session: Database session

    Returns:
        Updated task

    Raises:
        HTTPException: If user tries to update another user's task or task doesn't exist
    """
    # Verify that the requested user_id matches the authenticated user's ID
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only update your own tasks"
        )

    try:
        updated_task = TaskService.update_task(
            db=session,
            task_id=task_id,
            task_data=task_update,
            user_id=user_id
        )

        return updated_task

    except Exception as e:
        if "not found" in str(e).lower():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Task with ID {task_id} not found"
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An error occurred while updating the task: {str(e)}"
            )


@router.patch("/{user_id}/tasks/{task_id}/toggle", response_model=TaskPublic)
async def toggle_task_completion(
    user_id: int,
    task_id: int,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Toggle the completion status of a specific task for the authenticated user.

    Args:
        user_id: ID of the user toggling the task (should match authenticated user)
        task_id: ID of the task to toggle
        current_user: Currently authenticated user
        session: Database session

    Returns:
        Updated task with toggled completion status

    Raises:
        HTTPException: If user tries to toggle another user's task or task doesn't exist
    """
    # Verify that the requested user_id matches the authenticated user's ID
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only toggle your own tasks"
        )

    try:
        updated_task = TaskService.toggle_task_completion(
            db=session,
            task_id=task_id,
            user_id=user_id
        )

        return updated_task

    except Exception as e:
        if "not found" in str(e).lower():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Task with ID {task_id} not found"
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An error occurred while toggling the task: {str(e)}"
            )


@router.delete("/{user_id}/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    user_id: int,
    task_id: int,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Delete a specific task for the authenticated user.

    Args:
        user_id: ID of the user deleting the task (should match authenticated user)
        task_id: ID of the task to delete
        current_user: Currently authenticated user
        session: Database session

    Raises:
        HTTPException: If user tries to delete another user's task or task doesn't exist
    """
    # Verify that the requested user_id matches the authenticated user's ID
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only delete your own tasks"
        )

    try:
        success = TaskService.delete_task(
            db=session,
            task_id=task_id,
            user_id=user_id
        )

        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Task with ID {task_id} not found"
            )

    except Exception as e:
        if "not found" in str(e).lower():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Task with ID {task_id} not found"
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An error occurred while deleting the task: {str(e)}"
            )