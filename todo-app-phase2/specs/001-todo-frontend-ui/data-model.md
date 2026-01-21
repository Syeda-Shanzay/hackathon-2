# Data Model: Todo Full-Stack Web App

## Task Entity
- **id**: UUID/string (primary key)
- **title**: string (required, max 200 characters)
- **description**: string (optional, max 1000 characters)
- **status**: enum ['pending', 'completed'] (default: 'pending')
- **created_at**: datetime (auto-generated)
- **updated_at**: datetime (auto-generated)
- **due_date**: datetime (optional)
- **owner_id**: string/UUID (foreign key to user, required)

**Validation rules**:
- Title must be 1-200 characters
- Description must be 0-1000 characters if provided
- Status must be either 'pending' or 'completed'
- Owner_id must reference an existing user
- Due date must be in the future if provided

**State transitions**:
- 'pending' → 'completed' (when user marks task as complete)
- 'completed' → 'pending' (when user reopens task)

## User Entity (Managed by Better Auth)
- **id**: UUID/string (primary key, provided by auth system)
- **email**: string (unique, validated)
- **name**: string (optional)
- **created_at**: datetime (auto-generated)
- **updated_at**: datetime (auto-generated)

**Relationships**:
- One user to many tasks (one-to-many)
- Tasks are accessed only by their owner (enforced by backend middleware)

## API Request/Response Models

### Task Creation Request
- title (required)
- description (optional)
- due_date (optional)

### Task Response
- id
- title
- description
- status
- created_at
- updated_at
- due_date
- owner_id (filtered out in responses for security)

### Task Update Request
- title (optional)
- description (optional)
- status (optional)
- due_date (optional)