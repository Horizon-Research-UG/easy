"""Automation entry points for Python tooling."""

from __future__ import annotations

import pathlib
from typing import Sequence

import nox

PYTHON_VERSIONS: Sequence[str] = ("3.11",)
BACKEND_DIR = pathlib.Path("apps/backend")
SHARED_PYTHON_DIR = pathlib.Path("packages/python/shared")


@nox.session(python=PYTHON_VERSIONS)
def tests(session: nox.Session) -> None:
    session.run("poetry", "install", external=True)  # Was passiert: Abhängigkeiten installieren; Wer ruft wen: tests->session.run; Relevanz: Testumgebung.
    session.run("poetry", "run", "pytest", external=True)  # Was passiert: Tests ausführen; Wer ruft wen: tests->session.run->pytest; Relevanz: Qualität.


@nox.session(python=PYTHON_VERSIONS)
def lint(session: nox.Session) -> None:
    session.run("poetry", "install", "--with", "dev", external=True)  # Was passiert: Dev-Pakete installieren; Wer ruft wen: lint->session.run; Relevanz: Lint-Setup.
    session.run("poetry", "run", "ruff", "check", external=True)  # Was passiert: Ruff linten; Wer ruft wen: lint->session.run->ruff; Relevanz: Stilprüfung.


@nox.session(python=PYTHON_VERSIONS)
def typecheck(session: nox.Session) -> None:
    session.run("poetry", "install", "--with", "dev", external=True)  # Was passiert: Dev-Pakete installieren; Wer ruft wen: typecheck->session.run; Relevanz: Typ-Setup.
    session.run("poetry", "run", "mypy", external=True)  # Was passiert: Mypy prüfen; Wer ruft wen: typecheck->session.run->mypy; Relevanz: Typensicherheit.
