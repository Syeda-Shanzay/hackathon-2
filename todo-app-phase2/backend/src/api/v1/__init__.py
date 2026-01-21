"""
API v1 module for the Todo App
Contains version 1 API routes
"""
from fastapi import APIRouter

from . import tasks

# Create API v1 router
v1_router = APIRouter(prefix="/v1")

# Include all v1 routes
v1_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])