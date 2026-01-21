# Todo App API Documentation

## Base URL
All API endpoints are prefixed with `/api/v1`

## Authentication
Most endpoints require authentication. Include an Authorization header with a valid JWT token:
```
Authorization: Bearer <jwt-token>
```

## Endpoints

### Authentication

#### POST /auth/register
Register a new user

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securepassword123"
}
```

**Response:**
```json
{
  "id": "user-id",
  "email": "user@example.com",
  "access_token": "jwt-access-token",
  "refresh_token": "jwt-refresh-token"
}
```

#### POST /auth/login
Login a user

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securepassword123"
}
```

**Response:**
```json
{
  "id": "user-id",
  "email": "user@example.com",
  "access_token": "jwt-access-token",
  "refresh_token": "jwt-refresh-token"
}
```

### Tasks

#### GET /tasks
Get all tasks for the authenticated user

**Query Parameters:**
- `status`: Filter by status ('pending', 'completed', 'all')
- `sort`: Sort by ('date', 'title')
- `order`: Sort order ('asc', 'desc')

**Response:**
```json
[
  {
    "id": 1,
    "title": "Sample task",
    "description": "Task description",
    "status": "pending",
    "created_at": "2023-01-01T00:00:00",
    "updated_at": "2023-01-01T00:00:00",
    "due_date": "2023-01-02T00:00:00",
    "owner_id": 1
  }
]
```

#### POST /tasks
Create a new task

**Request Body:**
```json
{
  "title": "New task",
  "description": "Task description",
  "due_date": "2023-01-01T00:00:00"
}
```

**Response:**
```json
{
  "id": 1,
  "title": "New task",
  "description": "Task description",
  "status": "pending",
  "created_at": "2023-01-01T00:00:00",
  "updated_at": "2023-01-01T00:00:00",
  "due_date": "2023-01-01T00:00:00",
  "owner_id": 1
}
```

#### GET /tasks/{id}
Get a specific task

**Response:**
```json
{
  "id": 1,
  "title": "Sample task",
  "description": "Task description",
  "status": "pending",
  "created_at": "2023-01-01T00:00:00",
  "updated_at": "2023-01-01T00:00:00",
  "due_date": "2023-01-02T00:00:00",
  "owner_id": 1
}
```

#### PUT /tasks/{id}
Update a task

**Request Body:**
```json
{
  "title": "Updated task",
  "description": "Updated description",
  "status": "completed",
  "due_date": "2023-01-02T00:00:00"
}
```

**Response:**
```json
{
  "id": 1,
  "title": "Updated task",
  "description": "Updated description",
  "status": "completed",
  "created_at": "2023-01-01T00:00:00",
  "updated_at": "2023-01-01T00:00:00",
  "due_date": "2023-01-02T00:00:00",
  "owner_id": 1
}
```

#### DELETE /tasks/{id}
Delete a task

**Response:**
Status: 204 No Content

#### PATCH /tasks/{id}/complete
Mark a task as complete

**Response:**
```json
{
  "id": 1,
  "title": "Sample task",
  "description": "Task description",
  "status": "completed",
  "created_at": "2023-01-01T00:00:00",
  "updated_at": "2023-01-01T00:00:00",
  "due_date": "2023-01-02T00:00:00",
  "owner_id": 1
}
```

#### PATCH /tasks/{id}/reopen
Reopen a completed task

**Response:**
```json
{
  "id": 1,
  "title": "Sample task",
  "description": "Task description",
  "status": "pending",
  "created_at": "2023-01-01T00:00:00",
  "updated_at": "2023-01-01T00:00:00",
  "due_date": "2023-01-02T00:00:00",
  "owner_id": 1
}
```

## Error Responses

All error responses follow this format:
```json
{
  "detail": "Error message"
}
```

Common HTTP status codes:
- 200: OK
- 201: Created
- 204: No Content
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 409: Conflict
- 500: Internal Server Error