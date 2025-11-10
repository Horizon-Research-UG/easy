"""Health and metadata endpoints."""

from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["health"])  # Was passiert: Router definieren; Wer ruft wen: Modul->APIRouter; Relevanz: Endpunktgruppe.


@router.get("/", summary="Readiness probe")
async def readiness() -> dict[str, str]:
    """Simple readiness endpoint for orchestration probes."""

    return {"status": "ok"}  # Was passiert: Status antworten; Wer ruft wen: readiness liefert Dict; Relevanz: Monitoring.
