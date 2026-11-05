import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// Build output goes to ../dist so api/main.py can serve it in production.
export default defineConfig({
  plugins: [react()],
  build: { outDir: "../dist", emptyOutDir: true },
});
