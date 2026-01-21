# Todo App - Frontend & Backend Integration Guide

## Overview
This guide explains how to run the fully integrated Todo application with both frontend and backend components.

## Project Structure
```
todo-app-phase2/
├── backend/
│   └── src/
│       ├── api/
│       │   ├── main.py          # FastAPI application entry point
│       │   └── routes/
│       │       └── tasks.py     # Task API endpoints
│       ├── database/
│       │   └── database.py      # Database connection
│       ├── models/
│       │   ├── task.py          # Task model
│       │   └── user.py          # User model
│       ├── services/
│       │   └── task_service.py  # Business logic
│       └── utils/
│           ├── auth.py          # JWT utilities
│           └── logging.py       # Logging utilities
└── frontend/
    └── src/
        ├── app/
        │   ├── tasks/
        │   │   └── page.tsx     # Tasks page
        │   └── page.tsx         # Home page
        ├── components/
        │   ├── TaskList.tsx     # Task list component
        │   ├── TaskCard.tsx     # Task card component
        │   └── TaskForm.tsx     # Task form component
        ├── hooks/
        │   ├── useAuth.ts       # Authentication hook
        │   └── useTasks.ts      # Task management hook
        └── lib/
            └── api.ts           # API client
```

## Running the Application

### Backend Setup
1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Start the backend server:
```bash
cd src
uvicorn api.main:app --reload --port 8000
```

### Frontend Setup
1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the frontend development server:
```bash
npm run dev
```

## API Endpoints

The backend provides the following authenticated endpoints:

- `GET /api/{user_id}/tasks` - Get all tasks for a user
- `POST /api/{user_id}/tasks` - Create a new task
- `GET /api/{user_id}/tasks/{task_id}` - Get a specific task
- `PUT /api/{user_id}/tasks/{task_id}` - Update a task
- `PATCH /api/{user_id}/tasks/{task_id}/toggle` - Toggle task completion
- `DELETE /api/{user_id}/tasks/{task_id}` - Delete a task

## Authentication

- JWT tokens are required for all task operations
- Tokens are obtained via the Better Auth system from the frontend
- All API requests include the Authorization header: `Bearer {token}`
- 401 Unauthorized responses trigger a redirect to the login page

## Features

1. **User Authentication**: Integrated with Better Auth
2. **Task Management**: Full CRUD operations
3. **User Isolation**: Users can only access their own tasks
4. **Real-time Updates**: Task list updates after each operation
5. **Responsive UI**: Works on desktop and mobile devices
6. **Error Handling**: Proper error messages and validation
7. **Filtering & Sorting**: Tasks can be filtered by status and sorted

## Environment Variables

Frontend (.env.local):
- `NEXT_PUBLIC_API_BASE_URL`: Points to the backend server (default: http://localhost:8000)

Backend (.env):
- `DATABASE_URL`: Database connection string
- `BETTER_AUTH_SECRET`: JWT signing secret

## Troubleshooting

1. **CORS Issues**: Ensure the backend allows requests from the frontend origin
2. **Authentication Failures**: Verify JWT tokens are being passed correctly
3. **Database Connection**: Check that the database URL is configured properly
4. **Port Conflicts**: Make sure ports 3000 (frontend) and 8000 (backend) are available