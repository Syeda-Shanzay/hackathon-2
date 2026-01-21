---
description: "Task list for Todo Full-Stack Web App implementation"
---

# Tasks: Todo Frontend UI

**Input**: Design documents from `/specs/001-todo-frontend-ui/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: No explicit test requirements in feature specification - tests will not be included in this implementation.
**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `backend/src/`, `frontend/src/`

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure with backend/ and frontend/ directories
- [x] T002 [P] Initialize backend with FastAPI and SQLModel dependencies in backend/requirements.txt
- [x] T003 [P] Initialize frontend with Next.js 16+, TypeScript, and Tailwind CSS dependencies in frontend/package.json
- [x] T004 [P] Set up shared environment configuration for DATABASE_URL and BETTER_AUTH_SECRET

---
## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T005 Set up database schema and migrations framework in backend/src/database/
- [x] T006 [P] Implement Better Auth authentication framework with JWT and refresh tokens in backend/src/auth/
- [x] T007 [P] Create base models/entities that all stories depend on in backend/src/models/
- [x] T008 [P] Setup API routing and middleware structure in backend/src/api/
- [x] T009 Create API client utility in frontend/src/lib/api.ts
- [x] T010 Configure error handling and logging infrastructure in both frontend and backend
- [x] T011 Create TypeScript types for API entities in frontend/src/types/index.ts

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---
## Phase 3: User Story 1 - View and Manage Personal Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable logged-in users to view their tasks in a clean, organized way and perform basic CRUD operations on them.

**Independent Test**: Users can log in, view their existing tasks, create a new task, mark an existing task as complete, and delete a task. The feature delivers immediate value as a complete task management solution.

### Implementation for User Story 1

- [x] T012 [P] [US1] Create Task model in backend/src/models/task.py with id, title, description, status, created_at, updated_at, due_date, owner_id
- [x] T013 [P] [US1] Create Task service in backend/src/services/task_service.py with CRUD operations
- [x] T014 [US1] Implement task endpoints in backend/src/api/v1/tasks.py (GET all, POST create, PUT update, DELETE delete, PATCH complete/reopen)
- [x] T015 [P] [US1] Create TaskCard component in frontend/src/components/TaskCard.tsx with shadow, hover effects, and status badges
- [x] T016 [P] [US1] Create TaskList component in frontend/src/components/TaskList.tsx to display cards in grid layout
- [x] T017 [P] [US1] Create TaskForm component in frontend/src/components/TaskForm.tsx for adding/editing tasks
- [x] T018 [US1] Create tasks page in frontend/src/app/tasks/page.tsx to integrate components and API calls
- [x] T019 [US1] Add authentication middleware to verify JWT tokens and user ownership in backend/src/api/deps.py
- [x] T020 [US1] Implement user isolation to ensure users only see their own tasks in backend/src/services/task_service.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---
## Phase 4: User Story 2 - Filter and Sort Tasks (Priority: P2)

**Goal**: Enable logged-in users to filter and sort their tasks to find specific items quickly.

**Independent Test**: Users can apply filters and sorting options to their task list and see immediate visual updates reflecting their selections. This makes the task management more efficient.

### Implementation for User Story 2

- [x] T021 [P] [US2] Update task service to support filtering by status in backend/src/services/task_service.py
- [x] T022 [P] [US2] Update task service to support sorting by date and title in backend/src/services/task_service.py
- [x] T023 [US2] Enhance task endpoints with query parameters for filtering and sorting in backend/src/api/v1/tasks.py
- [x] T024 [P] [US2] Create filter controls component in frontend/src/components/FilterControls.tsx
- [x] T025 [P] [US2] Update TaskList component to support filtering and sorting in frontend/src/components/TaskList.tsx
- [x] T026 [US2] Add filtering and sorting functionality to tasks page in frontend/src/app/tasks/page.tsx

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---
## Phase 5: User Story 3 - Responsive Navigation and Authentication Flow (Priority: P3)

**Goal**: Enable users to navigate the application seamlessly across devices and manage their authentication state.

**Independent Test**: Users can log in, access different parts of the application through navigation, and log out. The interface adapts appropriately to different screen sizes.

### Implementation for User Story 3

- [x] T027 [P] [US3] Create Header component with navigation links in frontend/src/components/Header.tsx
- [x] T028 [P] [US3] Create Footer component in frontend/src/components/Footer.tsx
- [x] T029 [P] [US3] Create authentication hooks in frontend/src/hooks/useAuth.ts
- [x] T030 [US3] Create login page in frontend/src/app/login/page.tsx with Better Auth integration
- [x] T031 [US3] Create signup page in frontend/src/app/signup/page.tsx with Better Auth integration
- [x] T032 [US3] Create homepage/dashboard page in frontend/src/app/page.tsx
- [x] T033 [US3] Implement responsive design for all components using Tailwind CSS
- [x] T034 [US3] Add logout functionality in frontend/src/components/Header.tsx
- [x] T035 [US3] Implement token refresh mechanism for automatic background refresh in frontend/src/hooks/useAuth.ts

**Checkpoint**: All user stories should now be independently functional

---
## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T036 Add confirmation dialog for delete operations in frontend/src/components/TaskCard.tsx
- [x] T037 Add form validation with user-friendly error messages in frontend/src/components/TaskForm.tsx
- [x] T038 Add loading states for API operations in frontend/src/components/TaskList.tsx
- [x] T039 Add error handling UI for API failures in frontend/src/lib/api.ts
- [x] T040 Create consistent color palette and button styles in frontend/src/styles/
- [x] T041 Add accessibility features (focus states, semantic HTML) in all components
- [x] T042 Add subtle animations for user interactions in frontend/src/components/
- [x] T043 Run quickstart.md validation to ensure setup instructions work correctly
- [x] T044 Add comprehensive documentation for API endpoints in backend/
- [x] T045 Add performance optimizations for task loading and rendering

---
## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Builds upon US1 components
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---
## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---
## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence