---
id: 0002
title: todo-backend-api-plan
stage: plan
date: 2026-01-10
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-todo-backend-api
branch: 001-todo-backend-api
user: default
command: /sp.plan
labels: ["plan", "backend", "api", "todo-app", "task-management", "fastapi", "authentication"]
links:
  spec: /specs/001-todo-backend-api/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-todo-backend-api/plan.md
  - specs/001-todo-backend-api/research.md
  - specs/001-todo-backend-api/data-model.md
  - specs/001-todo-backend-api/contracts/openapi.yaml
  - specs/001-todo-backend-api/quickstart.md
tests:
  - none
---

## Prompt

Create a detailed step-by-step plan to implement the full-stack Todo app (frontend + backend) with authentication, database, and API integration using Next.js + FastAPI + Neon PostgreSQL. Ensure professional UI and smooth backend integration.

## Steps

### 1. Environment Setup
1. Verify Node.js, npm, Python, and pip are installed.
2. Create `.env.local` in frontend:
   - NEXT_PUBLIC_BETTER_AUTH_API_KEY=<your_key>
   - NEXT_PUBLIC_BETTER_AUTH_SECRET=<your_jwt_secret>
3. Create `.env` in backend:
   - DATABASE_URL=<Neon_PostgreSQL_connection_string>
   - BETTER_AUTH_SECRET=<same_jwt_secret_as_frontend>
4. Install required packages:
   - Frontend: Next.js, Tailwind CSS, Better Auth
   - Backend: FastAPI, SQLModel, psycopg, python-jose, Pydantic
5. Run frontend (`npm run dev`) and backend (`uvicorn main:app --reload`) to verify environment.

### 2. Backend Implementation
1. Create database connection (`db.py`) using SQLModel.
2. Define ORM models (`models.py`) for tasks and users.
3. Implement JWT verification middleware (`utils/auth.py`).
4. Create API endpoints (`routes/tasks.py`) as specified:
   - GET /tasks, POST /tasks, GET /tasks/{id}, PUT /tasks/{id}, DELETE /tasks/{id}, PATCH /tasks/{id}/complete
5. Filter all task queries by authenticated user.
6. Test each endpoint using Postman or curl.

### 3. Frontend Implementation
1. Create pages and layouts using Next.js App Router:
   - Home page, Dashboard, Task List, Task Form (Create/Edit)
2. Implement UI components with Tailwind CSS for professional look:
   - Buttons, Inputs, Cards, Modals
3. Implement API client (`lib/api.ts`) to call backend endpoints:
   - Attach JWT token in `Authorization: Bearer <token>` header
4. Connect Better Auth for login/signup:
   - Ensure JWT token is stored securely
5. Display tasks dynamically in task list:
   - Show title, status, created date, complete toggle, edit, delete

### 4. Integration
1. Connect frontend task components to backend API client.
2. Ensure task operations (create, update, delete, complete) update UI in real-time.
3. Handle JWT expiration gracefully:
   - If token expired → redirect to login
4. Ensure CORS is correctly configured on backend for frontend domain.
5. Test full flow:
   - Login → fetch tasks → create → edit → delete → toggle complete

### 5. Styling & UX
1. Use Tailwind utilities to create professional UI:
   - Cards for tasks, clear buttons, modals for forms
2. Add responsive design for desktop & mobile.
3. Ensure error messages and loading states are user-friendly.

### 6. Testing & Deployment
1. Test all frontend-backend flows locally.
2. Verify JWT authentication, database operations, task filtering.
3. Optional: Dockerize backend & frontend (if needed later)
4. Prepare for deployment on Venerel (frontend) + Neon PostgreSQL (backend).

## Deliverables
- Fully working frontend & backend integrated Todo app
- Professional UI with responsive design
- Backend secured with JWT
- API endpoints fully functional
- Environment variables configured
- Task CRUD fully implemented and tested
- Step-by-step folder structure with all files in place

## Response snapshot

Successfully created a comprehensive implementation plan for the Todo Backend API. The plan includes:

- Detailed technical context with language versions, dependencies, and performance goals
- Constitution compliance check confirming all requirements are met
- Project structure with clear separation of concerns between models, services, API routes, and utilities
- Research summary covering technology stack decisions and rationale
- Data model defining Task and User entities with relationships and validation rules
- API contracts in OpenAPI 3.0 format specifying all endpoints and request/response schemas
- Quickstart guide with setup instructions and API usage information
- Agent context updated with new technologies used in the project

The plan follows all requirements from the specification including JWT authentication, user isolation, FastAPI + SQLModel implementation, and Neon PostgreSQL database integration.

## Outcome

- ✅ Impact: Created comprehensive implementation plan covering all required aspects of the backend API
- 🧪 Tests: No automated tests for planning documents
- 📁 Files: Created plan.md, research.md, data-model.md, contracts/openapi.yaml, and quickstart.md in feature directory
- 🔁 Next prompts: Ready to proceed with task generation using /sp.tasks
- 🧠 Reflection: Plan addresses all requirements from user input including API endpoints, authentication, database, and integration with frontend.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin task generation to break down implementation into specific steps
