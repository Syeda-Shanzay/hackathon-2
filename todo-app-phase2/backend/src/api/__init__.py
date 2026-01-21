"""
API module for the Todo App
Contains API routing and middleware structure
"""
from fastapi import APIRouter

# Create main API router
api_router = APIRouter()

# Import and include all API routes
from .v1 import tasks  # noqa: F401

# Include the tasks router
from .v1.tasks import router as tasks_router
api_router.include_router(tasks_router, prefix="/tasks", tags=["tasks"])