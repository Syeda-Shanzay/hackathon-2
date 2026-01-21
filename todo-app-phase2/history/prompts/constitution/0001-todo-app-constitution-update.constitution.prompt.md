---
id: 0001
title: todo-app-constitution-update
stage: constitution
date: 2026-01-10
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: default
command: /sp.constitution
labels: ["constitution", "todo-app", "spec-driven", "governance"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - none
---

## Prompt

Constitution for Spec-Driven Phase II: Full-Stack Todo App.
  This document defines the rules, conventions, and constraints Claude Code
  must follow when implementing frontend, backend, authentication, and database features.
  It ensures consistent architecture, spec compliance, and secure practices.

rules:
  - Always read the relevant spec files before implementing a feature:
      - @specs/overview.md
      - @specs/features/task-crud.md
      - @specs/features/authentication.md
      - @specs/api/rest-endpoints.md
      - @specs/database/schema.md
      - @specs/ui/components.md
      - @specs/ui/pages.md
  - Do NOT implement code without explicit instructions from specs.
  - Enforce user isolation: every API request must be filtered by authenticated user_id.
  - JWT tokens issued by Better Auth must be verified in backend FastAPI endpoints.
  - Follow frontend conventions strictly:
      - Next.js 16+ App Router
      - Server components by default
      - Client components only for interactivity
      - API calls only through /lib/api.ts
      - Tailwind CSS for styling; no inline styles
  - Follow backend conventions strictly:
      - FastAPI + SQLModel
      - Database connection via DATABASE_URL environment variable
      - CRUD routes under /api/
      - Pydantic models for validation
      - Secure task operations: only owner can modify their tasks
  - Any change in schema or API must be confirmed against @specs/database/schema.md
  - Environment variables to be used consistently:
      - DATABASE_URL
      - BETTER_AUTH_SECRET
  - Maintain separation of concerns: frontend vs backend vs auth vs database
  - Always produce outputs consistent with Spec-Kit conventions
  - Flag any spec conflicts or missing details before proceeding

permissions:
  - Read and reference all spec files
  - Suggest schema updates only when required
  - Implement code only when instructed by user/prompt

workflow:
  - Step 1: Analyze specs for the feature or task
  - Step 2: Confirm user stories and acceptance criteria
  - Step 3: Implement backend or frontend as per CLAUDE.md guidelines
  - Step 4: Integrate JWT authentication securely
  - Step 5: Test & validate against specs
  - Step 6: Report completion or issues back to user

notes:
  - This constitution acts as the ultimate guideline for Claude Code in Phase II.
  - Use it as a reference whenever implementing any feature or endpoint.

## Response snapshot

Updated the project constitution with specific details for the Todo App Phase II project. The new constitution includes:

- Core Principles: Spec Compliance, User Isolation & Security, Frontend Architecture Standards, Backend Architecture Standards, Environment & Configuration Management, and Cross-Layer Consistency
- Additional Constraints: Technology stack requirements, Security requirements, and Performance standards
- Development Workflow: Feature Implementation Process, Code Review Requirements, and Quality Gates
- Governance: Rules for how the constitution is applied and updated

The constitution now specifically addresses Next.js 16+ with App Router, FastAPI + SQLModel, Neon Serverless PostgreSQL, Better Auth with JWT, and the requirement for user isolation in all API endpoints.

## Outcome

- ✅ Impact: Updated constitution now properly governs development for Todo App Phase II with specific technology stack and security requirements
- 🧪 Tests: No tests required for this documentation update
- 📁 Files: Updated .specify/memory/constitution.md with project-specific governance
- 🔁 Next prompts: Can now proceed with feature development following the updated constitution
- 🧠 Reflection: The constitution now properly reflects the specific requirements for the full-stack todo app with authentication and proper security measures.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
