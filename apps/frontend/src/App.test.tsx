import { afterEach, describe, expect, it, vi } from "vitest"; // Was passiert: Test-Hilfen importieren; Wer ruft wen: Modul->vitest; Relevanz: Testaufbau.
import { loadBtcPrice } from "./App"; // Was passiert: BTC-Lader holen; Wer ruft wen: Tests->App; Relevanz: Funktion prüfen.

describe("App smoke", () => { // Was passiert: Testsuite definieren; Wer ruft wen: Tests->describe; Relevanz: Gruppierung.
  it("passes", () => { // Was passiert: Einzeltest definieren; Wer ruft wen: describe->it; Relevanz: Baseline.
    expect(true).toBe(true); // Was passiert: Wahrheit prüfen; Wer ruft wen: it->expect; Relevanz: Toolkette ok.
  }); // Was passiert: Testfunktion schließen; Wer ruft wen: it->Callback Ende; Relevanz: Blockende.
}); // Was passiert: Suite schließen; Wer ruft wen: describe->Callback Ende; Relevanz: Blockende.

const originalFetch = globalThis.fetch;

afterEach(() => {
  globalThis.fetch = originalFetch;
  vi.restoreAllMocks();
});

describe("loadBtcPrice", () => {
  it("formats the returned price", async () => {
    const mockPayload = { bitcoin: { eur: 12345.67 } };
    globalThis.fetch = vi.fn().mockResolvedValue({
      ok: true,
      json: async () => mockPayload,
    }) as unknown as typeof fetch;

    const expected = new Intl.NumberFormat("de-DE", { style: "currency", currency: "EUR" }).format(
      mockPayload.bitcoin.eur,
    );

    await expect(loadBtcPrice()).resolves.toBe(expected);
  });

  it("throws if the response status is not ok", async () => {
    globalThis.fetch = vi.fn().mockResolvedValue({ ok: false, status: 500 }) as unknown as typeof fetch;

    await expect(loadBtcPrice()).rejects.toThrow("BTC price lookup failed: 500");
  });
});
