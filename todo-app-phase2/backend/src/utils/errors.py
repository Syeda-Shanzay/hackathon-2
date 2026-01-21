"""
Custom error handling module for the Todo App
Defines custom exceptions and error responses
"""
from fastapi import HTTPException, status


class TodoException(HTTPException):
    """Base exception class for todo app"""
    def __init__(self, detail: str, status_code: int = status.HTTP_400_BAD_REQUEST):
        super().__init__(status_code=status_code, detail=detail)


class TaskNotFoundException(TodoException):
    """Raised when a task is not found"""
    def __init__(self, task_id: int):
        super().__init__(
            detail=f"Task with ID {task_id} not found",
            status_code=status.HTTP_404_NOT_FOUND
        )


class UserNotFoundException(TodoException):
    """Raised when a user is not found"""
    def __init__(self, user_email: str):
        super().__init__(
            detail=f"User with email {user_email} not found",
            status_code=status.HTTP_404_NOT_FOUND
        )


class UnauthorizedAccessException(TodoException):
    """Raised when a user doesn't have access to a resource"""
    def __init__(self):
        super().__init__(
            detail="Unauthorized access to this resource",
            status_code=status.HTTP_403_FORBIDDEN
        )


class InvalidCredentialsException(TodoException):
    """Raised when invalid credentials are provided"""
    def __init__(self):
        super().__init__(
            detail="Invalid credentials",
            status_code=status.HTTP_401_UNAUTHORIZED
        )


class DuplicateEmailException(TodoException):
    """Raised when trying to create a user with an existing email"""
    def __init__(self):
        super().__init__(
            detail="A user with this email already exists",
            status_code=status.HTTP_409_CONFLICT
        )


# Error handler for FastAPI
from fastapi.responses import JSONResponse
from fastapi import Request


async def todo_exception_handler(request: Request, exc: TodoException):
    """Handle custom todo exceptions"""
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )