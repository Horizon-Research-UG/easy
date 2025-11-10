"""Smoke tests for the health endpoint."""

import pytest
from httpx import AsyncClient

from backend.main import app


@pytest.mark.asyncio
async def test_readiness_endpoint() -> None:
    async with AsyncClient(app=app, base_url="http://test") as client:  # Was passiert: Testclient öffnen; Wer ruft wen: Test->AsyncClient; Relevanz: API simulieren.
        response = await client.get("/health/")  # Was passiert: GET senden; Wer ruft wen: client->get; Relevanz: Endpoint prüfen.
    assert response.status_code == 200  # Was passiert: Status prüfen; Wer ruft wen: Assertion->response.status_code; Relevanz: Verfügbarkeit.
    assert response.json() == {"status": "ok"}  # Was passiert: Payload prüfen; Wer ruft wen: Assertion->response.json; Relevanz: Inhalt.
