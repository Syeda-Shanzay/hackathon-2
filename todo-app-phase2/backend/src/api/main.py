from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from ..database.database import create_db_and_tables
from .routes.tasks import router as tasks_router
from .routes.auth import router as auth_router


def create_application() -> FastAPI:
    """
    Create and configure the FastAPI application

    Returns:
        Configured FastAPI application instance
    """
    app = FastAPI(
        title="Todo Backend API",
        description="API for the Todo App backend service with authentication and task management",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json"
    )

    # CORS configuration for frontend integration
    frontend_origin = os.getenv("FRONTEND_ORIGIN", "http://localhost:3000")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[frontend_origin],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include API routes
    app.include_router(tasks_router, prefix="/api", tags=["tasks"])
    app.include_router(auth_router, prefix="/api/auth", tags=["auth"])

    @app.on_event("startup")
    def on_startup():
        """Create database tables on application startup"""
        create_db_and_tables()

    @app.get("/")
    def read_root():
        """Root endpoint for health check"""
        return {"message": "Todo Backend API is running"}

    @app.get("/health")
    def health_check():
        """Health check endpoint"""
        return {"status": "healthy", "service": "todo-backend-api"}

    return app


# Create the main application instance
app = create_application()


# For development/testing purposes
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)