# Data Model: Todo Backend API

## Task Entity
- **id**: UUID/int (primary key)
- **title**: string (required, max 200 characters)
- **description**: string (optional, max 1000 characters)
- **completed**: boolean (default: False)
- **created_at**: datetime (auto-generated)
- **updated_at**: datetime (auto-generated, updates on modification)
- **user_id**: int/UUID (foreign key to user, required)

**Validation rules**:
- Title must be 1-200 characters
- Description must be 0-1000 characters if provided
- Completed must be a boolean value
- user_id must reference an existing user
- created_at and updated_at are managed automatically

**State transitions**:
- completed: False → True (when task is marked as complete)
- completed: True → False (when task is reopened)

## User Entity (Managed by Better Auth)
- **id**: UUID/int (primary key, provided by auth system)
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

### Task Response
- id
- title
- description
- completed
- created_at
- updated_at
- user_id (filtered out in responses for security)

### Task Update Request
- title (optional)
- description (optional)
- completed (optional)

## Database Schema

### tasks table
- id (SERIAL PRIMARY KEY)
- title (VARCHAR(200) NOT NULL)
- description (TEXT)
- completed (BOOLEAN DEFAULT FALSE)
- created_at (TIMESTAMP WITH TIME ZONE DEFAULT NOW())
- updated_at (TIMESTAMP WITH TIME ZONE DEFAULT NOW())
- user_id (INTEGER REFERENCES users(id) ON DELETE CASCADE)

### users table (managed by Better Auth)
- id (SERIAL PRIMARY KEY)
- email (VARCHAR(255) UNIQUE NOT NULL)
- name (VARCHAR(255))
- created_at (TIMESTAMP WITH TIME ZONE DEFAULT NOW())
- updated_at (TIMESTAMP WITH TIME ZONE DEFAULT NOW())

## Indexes
- Index on user_id for efficient user-based queries
- Index on completed for filtering operations
- Index on created_at for sorting operations