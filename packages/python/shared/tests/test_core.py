from shared.core import ServiceInfo


def test_service_info_defaults() -> None:
    info = ServiceInfo(name="backend", version="0.1.0")  # Was passiert: Datensatz anlegen; Wer ruft wen: Test->ServiceInfo; Relevanz: Basisobjekt.
    assert info.description == ""  # Was passiert: Default prüfen; Wer ruft wen: Assertion->info.description; Relevanz: Felderwartung.
    assert info.name == "backend"  # Was passiert: Name prüfen; Wer ruft wen: Assertion->info.name; Relevanz: Identität.
