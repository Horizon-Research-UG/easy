"""Core system plugin wiring common routers."""

from fastapi import FastAPI

from backend.routers import health


def register(app: FastAPI) -> None:
    """Attach built-in system routes."""

    app.include_router(health.router)  # Was passiert: Router montieren; Wer ruft wen: register->include_router->health.router; Relevanz: Health-Endpoint aktivieren.
