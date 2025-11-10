# Easy Platform Monorepo

Modular platform combining a FastAPI backend and a Vite + React frontend. The repository is organised to enable pluggable features and future mixed-reality integrations.

## Structure

- `apps/backend`: FastAPI service, bootstrapped with a plugin registry.
- `apps/frontend`: Vite + React web client targeting the backend API.
- `packages/python`: Shared Python libraries for cross-service logic.
- `packages/js`: Shared TypeScript utilities for frontends.
- `tools`: Experiments and CLI helpers for rapid prototyping.

## Getting Started

1. Install Python 3.11 and Node.js 20 + pnpm.
2. Bootstrap the backend:
   ```bash
   cd apps/backend
   poetry install
   poetry run backend-api
   ```
3. In a new terminal, bootstrap the frontend:
   ```bash
   cd apps/frontend
   pnpm install
   pnpm dev
   ```
4. Visit `http://localhost:5173` to access the app. API calls are proxied to `http://localhost:8000`.

## Testing

- Backend: `cd apps/backend && poetry run pytest`
- Frontend: `cd apps/frontend && pnpm test`

## Deployment

- Frontend: push `main` to GitHub and the `Deploy Frontend` workflow publishes `apps/frontend/dist` to GitHub Pages.<br>
   Configure the backend URL via repository variable `VITE_API_BASE_URL` (for example `https://your-backend.example.com`).
- Backend: deploy `apps/backend` to a FastAPI-friendly host (Render, Fly.io, Azure). Expose the public URL in `VITE_API_BASE_URL` so the static frontend can reach it.

## Continuous Integration

GitHub Actions workflow (`.github/workflows/ci.yml`) runs linting and tests across the monorepo.

## Next Steps

- Add domain-specific plugins under `backend.plugins`.
- Create shared SDKs in `packages/` to power future clients (including VR/MR bridges).
- Expand the tool sandbox for rapid validation of new components.
