# Architecture Overview

## Goals

- Modular FastAPI backend with plugin mounting.
- Vite + React SPA with proxy to the backend.
- Shared packages for cross-cutting concerns.
- Room for VR/MR bridge integration via dedicated adapters.

## Backend

- `backend.main.create_app` composes middleware and loads plugins from `backend.plugins.registry`.
- Plugins expose a `register(app)` function to contribute routers, dependencies, or background tasks.
- Settings resolved via `pydantic-settings` to simplify environment overrides.

## Frontend

- Vite dev server proxies `/api` traffic to the backend.
- React application fetches health status and surfaces future XR status.
- Shared TypeScript utilities imported from `@easy/shared` (pnpm workspace alias).

## Future VR/MR Integration

- Add `backend.plugins.xr` to expose XR session negotiation endpoints.
- Extend `packages/js/shared` with WebXR helpers for device detection.
- Introduce dedicated `packages/python/xr` for simulation/testing harnesses.
- Provide sandbox demos under `tools/sandbox` for rapid experimentation.
