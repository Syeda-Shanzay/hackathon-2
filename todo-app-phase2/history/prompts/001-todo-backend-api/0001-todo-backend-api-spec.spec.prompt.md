---
id: 0001
title: todo-backend-api-spec
stage: spec
date: 2026-01-10
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-todo-backend-api
branch: 001-todo-backend-api
user: default
command: /sp.specify
labels: ["spec", "backend", "api", "todo-app", "task-management", "fastapi", "authentication"]
links:
  spec: /specs/001-todo-backend-api/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-todo-backend-api/spec.md
  - specs/001-todo-backend-api/checklists/requirements.md
tests:
  - none
---

## Prompt

Build a complete backend for the Todo App using FastAPI + SQLModel with Neon PostgreSQL database. Integrate authentication using Better Auth JWT tokens issued from the frontend. The backend must fully communicate with the frontend API client.

## Requirements
1. **API Endpoints**:
   - GET /api/{user_id}/tasks → List all tasks for authenticated user
   - POST /api/{user_id}/tasks → Create a new task
   - GET /api/{user_id}/tasks/{id} → Get task details
   - PUT /api/{user_id}/tasks/{id} → Update a task
   - DELETE /api/{user_id}/tasks/{id} → Delete a task
   - PATCH /api/{user_id}/tasks/{id}/complete → Toggle task completion

2. **Authentication**:
   - Verify JWT token sent from frontend via `Authorization: Bearer <token>` header
   - Extract user ID from token and ensure user can only access their own tasks
   - Return 401 Unauthorized if token missing or invalid

3. **Database**:
   - Tables:
     - users (managed by Better Auth, `id`, `email`, `name`, `created_at`)
     - tasks (`id`, `user_id`, `title`, `description`, `completed`, `created_at`, `updated_at`)
   - Connect to Neon PostgreSQL using DATABASE_URL from `.env`
   - Implement ORM models with SQLModel

4. **Business Logic**:
   - CRUD operations filtered by authenticated user
   - Task completion toggling
   - Validate input data (title required, description optional)
   - Return proper HTTP status codes (200, 201, 404, 401, etc.)

5. **Integration with Frontend**:
   - Backend must respond with JSON objects compatible with frontend API client
   - Ensure CORS setup for Next.js frontend
   - Use environment variables for JWT secret and database URL
   - Optional: Include filtering by status (`all`, `pending`, `completed`) and sorting by `created_at` or `title` for GET /tasks

6. **Structure & Files**:
   - main.py → FastAPI app + include routers + JWT middleware
   - models.py → SQLModel models for tasks
   - routes/tasks.py → All task API endpoints
   - db.py → Database connection logic
   - utils/auth.py → JWT verification utility
   - requirements.txt → FastAPI, SQLModel, psycopg, python-jose, pydantic

7. **Testing**:
   - Include minimal test endpoints to verify JWT and DB connectivity
   - Ensure backend works when frontend API client calls endpoints

## Deliverable
- Fully working FastAPI backend ready to run with `uvicorn main:app --reload`
- Backend fully integrated with frontend via API endpoints
- All code modularized and clean, using Pydantic models for request/response

## Additional Instructions
- Use async endpoints wherever possible
- Follow Python best practices
- Ensure code is production-ready and secure
- Provide clear comments where necessary for maintainability
- Output the complete folder structure with all files, imports, and sample code

## Response snapshot

Successfully created a comprehensive specification for the Todo Backend API feature. The specification includes:

- Three prioritized user stories covering core functionality (P1: Access Personal Tasks, P2: Task Management Operations, P3: Secure Authentication & Authorization)
- Detailed acceptance scenarios for each user story
- 15 functional requirements covering API endpoints, authentication, database, validation, and performance
- Key entities (Task and User) with their properties
- Six measurable success criteria with specific metrics
- Edge cases including token expiration, database failures, and missing resources
- Quality checklist confirming all requirements are met

The specification follows the template structure and focuses on user value rather than implementation details.

## Outcome

- ✅ Impact: Created comprehensive spec for todo backend API with clear user stories and requirements
- 🧪 Tests: No automated tests for specification document
- 📁 Files: Created spec.md and requirements checklist in feature directory
- 🔁 Next prompts: Ready to proceed with planning phase using /sp.plan
- 🧠 Reflection: Specification addresses all requirements from user input including API endpoints, authentication, database, and integration with frontend.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin planning phase to design implementation approach
