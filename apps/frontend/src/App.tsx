import { useEffect, useState } from "react";

interface HealthResponse {
  status: string;
}

const MENU_ITEMS = ["Initiieren", "Spielen", "Komprimieren"]; // Was passiert: Menüoptionen definieren; Wer ruft wen: Modul initialisiert Array; Relevanz: UI-Auswahl.
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "/api"; // Was passiert: API-Basis setzen; Wer ruft wen: Modul liest Env; Relevanz: Deployment.

const loadHealth = async (): Promise<string> => {
  const response = await fetch(`${API_BASE_URL.replace(/\/$/, "")}/health/`); // Was passiert: Ziel bauen; Wer ruft wen: loadHealth->fetch; Relevanz: Statusquelle.
  if (!response.ok) throw new Error(`Health check failed: ${response.status}`); // Was passiert: Fehler werfen; Wer ruft wen: loadHealth->Error; Relevanz: Fehlerpfad.
  const data = (await response.json()) as HealthResponse; // Was passiert: JSON parsen; Wer ruft wen: loadHealth->response.json; Relevanz: Typisierung.
  return data.status; // Was passiert: Status liefern; Wer ruft wen: loadHealth beendet; Relevanz: Anzeige.
};

export default function App() {
  const [health, setHealth] = useState<string>("loading..."); // Was passiert: State anlegen; Wer ruft wen: App->useState; Relevanz: UI-Daten.
  useEffect(() => {
    loadHealth().then(setHealth).catch((error: Error) => setHealth(error.message)); // Was passiert: Health laden; Wer ruft wen: useEffect->loadHealth; Relevanz: Initialisierung.
  }, []); // Was passiert: Effekt Abhängigkeiten definieren; Wer ruft wen: App->useEffect; Relevanz: Einmalige Ausführung.
  return (
    <main>
      {/* Was passiert: Hauptcontainer zeichnen; Wer ruft wen: App->main; Relevanz: Layout. */}
      <section>
        {/* Was passiert: Inhalt bündeln; Wer ruft wen: App->section; Relevanz: Struktur. */}
        <h1>Easy Platform</h1>
        {/* Was passiert: Überschrift zeigen; Wer ruft wen: App->h1; Relevanz: Branding. */}
        <p>Backend health status: {health}</p>
        {/* Was passiert: Status rendern; Wer ruft wen: App->p; Relevanz: Monitoring. */}
        <nav>
          {/* Was passiert: Menücontainer; Wer ruft wen: App->nav; Relevanz: Navigation. */}
          <h2>Hauptmenü</h2>
          {/* Was passiert: Menüüberschrift; Wer ruft wen: App->h2; Relevanz: Orientierung. */}
          <ul>
            {/* Was passiert: Liste darstellen; Wer ruft wen: App->ul; Relevanz: Optionen. */}
            {MENU_ITEMS.map((label) => (
              <li key={label}>
                {/* Was passiert: Eintrag kapseln; Wer ruft wen: map->li; Relevanz: Struktur. */}
                <button type="button">{label}</button>
                {/* Was passiert: Aktion anbieten; Wer ruft wen: map->button; Relevanz: Interaktion. */}
              </li>
            ))}
          </ul>
        </nav>
        <p>VR/MR bridge ready: coming soon 🔮</p>
        {/* Was passiert: VR Hinweis; Wer ruft wen: App->p; Relevanz: Roadmap. */}
      </section>
    </main>
  );
}
