<!-- SYNC IMPACT REPORT
Version change: 1.0.0 → 1.1.0
Modified principles: None (new constitution)
Added sections: All sections specific to Todo App
Removed sections: None
Templates requiring updates: ⚠ pending - .specify/templates/plan-template.md, .specify/templates/spec-template.md, .specify/templates/tasks-template.md
Follow-up TODOs: None
-->

# Todo App Phase II Constitution

## Core Principles

### I. Spec Compliance
All development must strictly adhere to the defined specifications. Before implementing any feature, read and understand the relevant spec files: @specs/overview.md, @specs/features/task-crud.md, @specs/features/authentication.md, @specs/api/rest-endpoints.md, @specs/database/schema.md, @specs/ui/components.md, @specs/ui/pages.md. Flag any missing details, inconsistencies, or conflicts in the specs before proceeding.

### II. User Isolation & Security
Every API request must be filtered by authenticated user_id to ensure users can only access and modify their own tasks. JWT tokens issued by Better Auth must be verified in backend FastAPI endpoints. This is a non-negotiable security requirement that must be enforced in all API endpoints.

### III. Frontend Architecture Standards
Follow Next.js 16+ App Router conventions strictly: use Server components by default, Client components only for interactivity, API calls only through /lib/api.ts, and Tailwind CSS for styling with no inline styles. This ensures consistent frontend architecture and maintainability.

### IV. Backend Architecture Standards
Implement backend using FastAPI + SQLModel with database connection via DATABASE_URL environment variable. CRUD routes must be under /api/, use Pydantic models for validation, and enforce secure task operations where only the owner can modify their tasks. This maintains consistent backend patterns.

### V. Environment & Configuration Management
Consistently use required environment variables: DATABASE_URL and BETTER_AUTH_SECRET. Maintain separation of concerns between frontend, backend, authentication, and database layers. Always produce outputs consistent with Spec-Kit conventions.

### VI. Cross-Layer Consistency
Ensure frontend, backend, authentication, and database are always aligned. Verify that API endpoints match database models and UI requirements. Any deviation between layers must be flagged immediately to maintain system integrity.

## Additional Constraints

Technology stack requirements:
- Frontend: Next.js 16+ with App Router
- Backend: Python FastAPI + SQLModel
- Database: Neon Serverless PostgreSQL
- Authentication: Better Auth with JWT
- Styling: Tailwind CSS
- API: REST endpoints with JWT authentication

Security requirements:
- All API requests must include JWT tokens
- User isolation: each user sees only their own tasks
- Proper validation and sanitization of all inputs
- Secure handling of environment variables

Performance standards:
- Efficient database queries with proper indexing
- Optimized API responses
- Minimal client-side JavaScript where possible

## Development Workflow

### Feature Implementation Process:
1. Analyze specs for the feature or task
2. Confirm user stories and acceptance criteria
3. Implement backend or frontend as per CLAUDE.md guidelines
4. Integrate JWT authentication securely
5. Test & validate against specs
6. Report completion or issues back to user

### Code Review Requirements:
- All PRs must verify compliance with this constitution
- Verify that all changes maintain user isolation
- Confirm proper JWT authentication implementation
- Ensure consistency with frontend and backend architecture standards
- Validate that database schema changes align with spec requirements

### Quality Gates:
- All features must be implemented according to spec files
- No implementation without explicit spec guidance
- Proper error handling and validation in all API endpoints
- Comprehensive testing coverage for new features

## Governance

This constitution supersedes all other practices and development guidelines for the Todo App Phase II project. All development activities must comply with these principles and constraints. Amendments to this constitution require explicit documentation, approval from project stakeholders, and a clear migration plan for any breaking changes.

All PRs and code reviews must verify compliance with this constitution. Complexity must be justified with clear reasoning in the implementation approach. Use CLAUDE.md files for runtime development guidance and reference the spec files for feature requirements.

**Version**: 1.1.0 | **Ratified**: 2026-01-10 | **Last Amended**: 2026-01-10