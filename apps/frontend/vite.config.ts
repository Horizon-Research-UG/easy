import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

const basePath = process.env.BASE_PATH ?? "/"; // Was passiert: Basis-Pfad festlegen; Wer ruft wen: Build-Tool liest Env; Relevanz: GitHub Pages.

export default defineConfig({
  base: basePath,
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      "/api": {
        target: "http://localhost:8000",
        changeOrigin: true,
  rewrite: (path: string) => path.replace(/^\/api/, "")
      }
    }
  },
  build: {
    sourcemap: true
  }
});
