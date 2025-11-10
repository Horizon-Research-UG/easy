"""Application factory for the Easy backend service."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import get_settings
from .plugins import load_plugins, register_plugins


def create_app() -> FastAPI:
    """Instantiate the FastAPI application with configured middleware and plugins."""

    settings = get_settings()  # Was passiert: Einstellungen laden; Wer ruft wen: create_app->get_settings; Relevanz: Basisparameter.
    app = FastAPI(title=settings.app_name, debug=settings.debug)  # Was passiert: App erzeugen; Wer ruft wen: create_app->FastAPI; Relevanz: API-Hülle.
    cors_args = {"allow_origins": settings.allowed_origins, "allow_credentials": True, "allow_methods": ["*"], "allow_headers": ["*"]}  # Was passiert: CORS-Optionen bündeln; Wer ruft wen: create_app nutzt Einstellungen; Relevanz: Browserzugriff.
    app.add_middleware(CORSMiddleware, **cors_args)  # Was passiert: Middleware registrieren; Wer ruft wen: create_app->add_middleware->CORSMiddleware; Relevanz: Sicherheit.
    register_plugins(app, load_plugins())  # Was passiert: Plugins einbinden; Wer ruft wen: create_app->register_plugins->load_plugins; Relevanz: Modularität.
    return app  # Was passiert: App zurückgeben; Wer ruft wen: create_app beendet; Relevanz: Einstiegspunkt.


app = create_app()  # Was passiert: App-Fabrik ausführen; Wer ruft wen: Modul->create_app; Relevanz: ASGI-Export.


def run() -> None:
    """Launch the development server using uvicorn."""

    import uvicorn  # Was passiert: Servermodul laden; Wer ruft wen: run->import uvicorn; Relevanz: Startfunktion.

    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)  # Was passiert: Server starten; Wer ruft wen: run->uvicorn.run; Relevanz: Dev-Server.
