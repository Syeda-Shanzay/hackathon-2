# Feature Specification: Todo Backend API

**Feature Branch**: `001-todo-backend-api`
**Created**: 2026-01-10
**Status**: Draft
**Input**: User description: "Build a complete backend for the Todo App using FastAPI + SQLModel with Neon PostgreSQL database. Integrate authentication using Better Auth JWT tokens issued from the frontend. The backend must fully communicate with the frontend API client."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Access Personal Tasks (Priority: P1)

Logged-in users need to access their personal tasks through API endpoints. Users can list, create, update, delete, and mark tasks as complete/incomplete. The system verifies JWT tokens and ensures users only access their own tasks.

**Why this priority**: This is the core functionality of the todo app backend - users need to be able to manage their tasks via API to derive value from the application.

**Independent Test**: Users can authenticate with a JWT token, access their task list, create a new task, update an existing task, mark a task as complete, and delete a task. The feature delivers immediate value as a complete task management API.

**Acceptance Scenarios**:

1. **Given** user has a valid JWT token and owns tasks, **When** user calls GET /api/{user_id}/tasks, **Then** only tasks belonging to the user are returned in the response
2. **Given** user has a valid JWT token, **When** user calls POST /api/{user_id}/tasks with valid task data, **Then** a new task is created and assigned to the user

---

### User Story 2 - Task Management Operations (Priority: P2)

Logged-in users need to perform full CRUD operations on their tasks. Users can retrieve individual tasks, update task details, delete tasks, and toggle task completion status. The system ensures proper authentication and user isolation.

**Why this priority**: This enhances the core functionality by providing complete task management capabilities, allowing users to maintain their task lists effectively.

**Independent Test**: Users can retrieve a specific task by ID, update task details, delete unwanted tasks, and toggle completion status. Each operation respects user boundaries and authentication requirements.

**Acceptance Scenarios**:

1. **Given** user has a valid JWT token and owns a specific task, **When** user calls GET /api/{user_id}/tasks/{id}, **Then** only that specific task is returned
2. **Given** user has a valid JWT token and owns a specific task, **When** user calls PUT /api/{user_id}/tasks/{id} with updated data, **Then** the task is updated with new information

---

### User Story 3 - Secure Authentication & Authorization (Priority: P3)

The system must securely verify JWT tokens and enforce user isolation. Only authenticated users can access the API, and each user can only access their own data. The system properly handles authentication failures.

**Why this priority**: Essential for security and privacy - the backend must protect user data and prevent unauthorized access to tasks belonging to other users.

**Independent Test**: When a user provides an invalid JWT token, the system returns a 401 Unauthorized response. When a user attempts to access tasks belonging to another user, the system returns an appropriate error response.

**Acceptance Scenarios**:

1. **Given** user provides an invalid or expired JWT token, **When** user calls any task endpoint, **Then** the system returns a 401 Unauthorized response
2. **Given** user has a valid JWT token but attempts to access tasks owned by a different user, **When** user calls GET /api/{other_user_id}/tasks, **Then** the system returns an appropriate error indicating unauthorized access

---

### Edge Cases

- What happens when the JWT token expires during an API request? The system should reject the request with a 401 Unauthorized response.
- How does the system handle database connection failures? The system should return appropriate error responses to the frontend.
- What occurs when a user attempts to access a task that no longer exists? The system should return a 404 Not Found response.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST verify JWT tokens sent in Authorization header with format "Bearer <token>"
- **FR-002**: System MUST ensure users can only access their own tasks based on user ID extracted from JWT token
- **FR-003**: Users MUST be able to list all their tasks via GET /api/{user_id}/tasks endpoint
- **FR-004**: Users MUST be able to create new tasks via POST /api/{user_id}/tasks endpoint with title (required) and description (optional)
- **FR-005**: Users MUST be able to retrieve specific tasks via GET /api/{user_id}/tasks/{id} endpoint
- **FR-006**: Users MUST be able to update tasks via PUT /api/{user_id}/tasks/{id} endpoint
- **FR-007**: Users MUST be able to delete tasks via DELETE /api/{user_id}/tasks/{id} endpoint
- **FR-008**: Users MUST be able to toggle task completion status via PATCH /api/{user_id}/tasks/{id}/complete endpoint
- **FR-009**: System MUST connect to Neon PostgreSQL database using DATABASE_URL environment variable
- **FR-010**: System MUST use SQLModel for database ORM operations
- **FR-011**: System MUST return appropriate HTTP status codes (200, 201, 401, 404, etc.)
- **FR-012**: System MUST validate required input data (title required for new tasks)
- **FR-013**: System MUST support optional filtering by status (all, pending, completed) and sorting (by created_at or title) for GET /tasks endpoint
- **FR-014**: System MUST handle CORS for integration with Next.js frontend
- **FR-015**: System MUST be implemented with async endpoints for performance

### Key Entities

- **Task**: Represents a user's to-do item with properties: id, user_id (foreign key), title (required), description (optional), completed (boolean), created_at, updated_at
- **User**: Represents an authenticated user managed by Better Auth with properties: id, email, name, created_at (user data is referenced by tasks through user_id)

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can perform CRUD operations on their tasks with API response times under 500ms for 95% of requests
- **SC-002**: 99% of authenticated API requests successfully return the expected data
- **SC-003**: Users can create new tasks with 95% success rate on their first attempt
- **SC-004**: Authentication verification completes within 100ms for 99% of requests
- **SC-005**: The API handles 1000 concurrent users without degradation in performance
- **SC-006**: Users can successfully retrieve their task lists with 99% success rate
