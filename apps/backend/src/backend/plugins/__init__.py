"""Lightweight plugin system for registering modular service components."""

from __future__ import annotations

from collections.abc import Iterable
from importlib import import_module
from types import ModuleType
from typing import Protocol

from fastapi import FastAPI


class Plugin(Protocol):
    """Contract shared by backend plugin modules."""

    def register(self, app: FastAPI) -> None:  # pragma: no cover - interface only
        """Hook called during application startup to mount routes or dependencies."""


def load_plugins(path: str = "backend.plugins.registry") -> Iterable[Plugin]:
    """Dynamically load plugin modules from a registry module."""

    module = import_module(path)  # Was passiert: Modul laden; Wer ruft wen: load_plugins->import_module; Relevanz: Registry holen.
    exported = getattr(module, "__all__", [])  # Was passiert: Exportliste greifen; Wer ruft wen: load_plugins->getattr; Relevanz: Plugin-Namen.
    candidates = (getattr(module, name) for name in exported)  # Was passiert: Module iterieren; Wer ruft wen: load_plugins->getattr; Relevanz: Plugin-Objekte.
    plugins = [item for item in candidates if isinstance(item, ModuleType) and hasattr(item, "register")]  # Was passiert: gültige Plugins filtern; Wer ruft wen: load_plugins->List Comprehension; Relevanz: Schnittstelle sichern.
    return plugins  # Was passiert: Pluginliste zurückgeben; Wer ruft wen: load_plugins beendet; Relevanz: Weiterverarbeitung.


def register_plugins(app: FastAPI, plugins: Iterable[Plugin]) -> None:
    """Attach discovered plugins to the API application."""

    for plugin in plugins:  # Was passiert: Plugins durchlaufen; Wer ruft wen: register_plugins iteriert; Relevanz: Initialisierung.
        plugin.register(app)  # Was passiert: Plugin-Hook ausführen; Wer ruft wen: plugin.register; Relevanz: Routen anmelden.
