# Quickstart Guide: Todo Full-Stack Web App

## Prerequisites
- Node.js 18+ installed
- Python 3.11+ installed
- PostgreSQL (or Neon Serverless account)
- pnpm or npm package manager

## Environment Setup
1. Clone the repository
2. Create `.env` file in both frontend and backend directories with:
   ```
   # Backend
   DATABASE_URL="postgresql://username:password@host:port/database"
   BETTER_AUTH_SECRET="your-secret-key-here"

   # Frontend
   NEXT_PUBLIC_API_BASE_URL="http://localhost:8000"
   ```

## Backend Setup
1. Navigate to the `backend` directory
2. Install dependencies: `pip install -r requirements.txt`
3. Run database migrations: `python -m src.database.migrate`
4. Start the server: `uvicorn src.main:app --reload`

## Frontend Setup
1. Navigate to the `frontend` directory
2. Install dependencies: `pnpm install` or `npm install`
3. Start the development server: `pnpm dev` or `npm run dev`
4. Visit `http://localhost:3000` in your browser

## Running Tests
- Backend tests: `pytest tests/`
- Frontend tests: `pnpm test` or `npm run test`

## API Documentation
The API documentation is available at `http://localhost:8000/docs` when the backend is running.

## Authentication
1. Register a new user at `/register`
2. Login at `/login` to get your JWT token
3. The token will be stored in your browser and used automatically for protected requests

## Development Tips
- The frontend uses Next.js App Router with server and client components
- API calls are made through `lib/api.ts` which handles authentication headers
- All task operations are restricted to the authenticated user's own tasks