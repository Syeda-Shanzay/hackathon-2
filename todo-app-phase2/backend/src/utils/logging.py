"""
Logging utility module for the Todo App
Provides standardized logging across the application
"""
import logging
from logging.handlers import RotatingFileHandler
import os
from pathlib import Path
import json
from datetime import datetime


def setup_logging(log_level=logging.INFO):
    """
    Set up logging configuration for the application
    """
    # Create logs directory if it doesn't exist
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    # Create logger
    logger = logging.getLogger("todo_app")
    logger.setLevel(log_level)

    # Prevent adding handlers multiple times
    if logger.handlers:
        return logger

    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)

    # File handler with rotation
    file_handler = RotatingFileHandler(
        "logs/todo_app.log",
        maxBytes=10 * 1024 * 1024,  # 10 MB
        backupCount=5
    )
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


def log_error(error, context="", user_id=None):
    """
    Log an error with context information

    Args:
        error: Exception that occurred
        context: Additional context about where the error occurred
        user_id: ID of the user associated with the error (if applicable)
    """
    logger = logging.getLogger("error")
    user_info = f"User: {user_id}" if user_id else "User: Anonymous"

    logger.error(
        f"Error in {context}: {str(error)} - {user_info}",
        exc_info=True  # Include traceback
    )


# Create the main logger instance
logger = setup_logging()

# Export the logger
__all__ = ["logger", "log_error"]