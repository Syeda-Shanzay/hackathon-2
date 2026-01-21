"""
Main entry point for the Todo App API
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import create_db_and_tables
from .utils.logging import logger
from .utils.errors import todo_exception_handler, TodoException
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from .api.routes.tasks import router as tasks_router
from .api.routes.auth import router as auth_router

def create_application() -> FastAPI:
    """Create and configure the FastAPI application"""

    app = FastAPI(
        title="Todo App API",
        description="A full-featured todo application API",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # In production, replace with specific origins
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include API routes
    app.include_router(tasks_router, prefix="/api")
    app.include_router(auth_router, prefix="/api/auth", tags=["auth"])

    # Add custom exception handler
    app.add_exception_handler(TodoException, todo_exception_handler)

    @app.on_event("startup")
    def startup_event():
        """Initialize database tables on startup"""
        logger.info("Starting up Todo App API")
        try:
            create_db_and_tables()
            logger.info("Database initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing database: {str(e)}")
            raise

    @app.get("/")
    def read_root():
        """Health check endpoint"""
        return {"status": "healthy", "message": "Todo App API is running"}

    return app


# Create the main application instance
app = create_application()

# For uvicorn to run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)