import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./styles.css";

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render( // Was passiert: Root erzeugen; Wer ruft wen: main->createRoot.render; Relevanz: Mountpoint.
  <React.StrictMode>
    {/* Was passiert: StrictMode aktivieren; Wer ruft wen: main->React.StrictMode; Relevanz: Dev-Hinweise. */}
    <App />
    {/* Was passiert: App mounten; Wer ruft wen: main->App; Relevanz: UI Einstieg. */}
  </React.StrictMode>
);
