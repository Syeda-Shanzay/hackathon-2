---
id: 0001
title: todo-frontend-ui-spec
stage: spec
date: 2026-01-10
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-todo-frontend-ui
branch: 001-todo-frontend-ui
user: default
command: /sp.specify
labels: ["spec", "frontend", "ui", "todo-app", "task-management"]
links:
  spec: /specs/001-todo-frontend-ui/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-todo-frontend-ui/spec.md
  - specs/001-todo-frontend-ui/checklists/requirements.md
tests:
  - none
---

## Prompt

This Spec-Kit Plus prompt guides Claude Code to implement the frontend of Phase II:
  Full-Stack Todo Web App. The UI should be modern, professional, responsive, and
  aligned with the specifications in /specs/ui and /specs/features/task-crud.md.
  Use Next.js 16+ App Router, Tailwind CSS, and best UI/UX practices.

instructions:
  - Read all relevant UI and feature specs first:
      - @specs/ui/components.md
      - @specs/ui/pages.md
      - @specs/features/task-crud.md
      - @specs/features/authentication.md
  - Create a responsive layout:
      - Header with logo, navigation links (Home, Tasks, Profile, Logout)
      - Sidebar (optional) for navigation or filters
      - Main content area for task list and actions
      - Footer (optional)
  - Implement professional UI elements:
      - Card-style task items with shadow, hover effect, and clear spacing
      - Buttons with consistent color palette and hover states
      - Input fields with labels, placeholders, and proper validation styling
      - Task status badges (completed / pending) with distinguishable colors
  - Features to implement:
      - Display all tasks for logged-in user
      - Add new task with modal or inline form
      - Edit task inline or in modal
      - Delete task with confirmation prompt
      - Mark task as complete (toggle) with visual feedback
      - Filtering tasks by status: all / completed / pending
      - Sorting tasks by created date or title
  - Ensure accessibility and professional design:
      - Use semantic HTML tags
      - Include focus states for interactive elements
      - Responsive on mobile, tablet, and desktop
  - All API calls must go through /lib/api.ts
  - Tailwind CSS utility classes only; no inline styles
  - Split components logically:
      - /components/TaskCard.tsx
      - /components/TaskList.tsx
      - /components/TaskForm.tsx
      - /components/Header.tsx
      - /components/Footer.tsx
      - /components/Sidebar.tsx (optional)
  - Follow Next.js App Router conventions for pages:
      - /app/page.tsx for dashboard/home
      - /app/tasks/page.tsx for tasks listing
      - /app/tasks/[id]/page.tsx for task detail/edit
      - /app/login/page.tsx and /app/signup/page.tsx for auth
  - Use clear folder structure, proper imports, and maintain readability
  - Add subtle animations where appropriate (hover, button click, modal open)

permissions:
  - Generate new frontend components based on specs
  - Suggest color palette and UI improvements
  - Integrate with backend API endpoints securely
  - Follow design best practices for professional UI

workflow:
  - Step 1: Analyze frontend specs
  - Step 2: Generate layout & page structure
  - Step 3: Build reusable components
  - Step 4: Connect components to API client
  - Step 5: Test UI responsiveness and task functionality
  - Step 6: Review and refine styling

notes:
  - Claude Code should always follow the sp.constitution rules
  - Ensure task ownership and JWT authentication is respected in UI flows
  - Focus on creating a **clean, modern, professional, and beautiful UI**

## Response snapshot

Created a comprehensive specification for the Todo Frontend UI feature. The spec includes:

- Three prioritized user stories covering core functionality (P1: Task management, P2: Filtering/sorting, P3: Navigation/auth)
- Detailed acceptance scenarios for each user story
- 12 functional requirements covering task CRUD operations, authentication, responsiveness, and accessibility
- Key entity definition (Task)
- Six measurable success criteria with specific metrics
- Edge cases including JWT token expiration which requires clarification

The specification follows the template structure and focuses on user value rather than implementation details. A quality checklist was also created at specs/001-todo-frontend-ui/checklists/requirements.md.

## Outcome

- ✅ Impact: Created comprehensive spec for todo frontend UI with clear user stories and requirements
- 🧪 Tests: No automated tests for specification document
- 📁 Files: Created spec.md and requirements checklist in feature directory
- 🔁 Next prompts: Need to resolve JWT token expiration clarification before proceeding to planning phase
- 🧠 Reflection: Specification covers the core requirements while maintaining focus on user experience and business value.

## Evaluation notes (flywheel)

- Failure modes observed: One requirement needs clarification (JWT token handling)
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Clarify JWT token expiration handling requirement
