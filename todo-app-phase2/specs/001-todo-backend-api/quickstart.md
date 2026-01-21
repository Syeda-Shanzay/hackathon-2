# Quickstart Guide: Todo Backend API

## Prerequisites
- Python 3.11+ installed
- PostgreSQL (or Neon Serverless account)
- pip package manager
- Node.js and npm (for frontend integration testing)

## Environment Setup
1. Clone the repository
2. Create a `.env` file in the backend root directory with:
   ```
   DATABASE_URL="postgresql://username:password@host:port/database"
   BETTER_AUTH_SECRET="your-super-secret-jwt-key-here"
   ```

## Backend Setup
1. Navigate to the `backend` directory
2. Install dependencies: `pip install -r requirements.txt`
3. Set up the database: `python -c "from src.database import create_db_and_tables; create_db_and_tables()"`
4. Start the server: `uvicorn src.api.main:app --reload`

## API Endpoints
The API provides the following endpoints:
- `GET /{user_id}/tasks` - Retrieve all tasks for a user
- `POST /{user_id}/tasks` - Create a new task for a user
- `GET /{user_id}/tasks/{id}` - Get a specific task
- `PUT /{user_id}/tasks/{id}` - Update a task
- `DELETE /{user_id}/tasks/{id}` - Delete a task
- `PATCH /{user_id}/tasks/{id}/complete` - Toggle task completion status

## Authentication
All endpoints require a JWT token in the Authorization header:
`Authorization: Bearer <your-jwt-token>`

## Running Tests
- Backend tests: `pytest tests/`
- Test the API with curl or Postman, ensuring to include the JWT token

## Integration with Frontend
The backend is designed to work with the frontend API client located at `frontend/src/lib/api.ts`. The client should send JWT tokens in the Authorization header for all requests.

## Development Tips
- The backend uses FastAPI which provides automatic API documentation at `/docs` when running
- All database operations use SQLModel for type safety and validation
- Remember to validate that user_id in the URL path matches the user_id from the JWT token