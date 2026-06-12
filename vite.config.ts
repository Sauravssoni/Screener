import tailwindcss from '@tailwindcss/vite';
import react from '@vitejs/plugin-react';
import path from 'path';
import { defineConfig } from 'vite';
import express from 'express';

// A simple Vite plugin to serve the /reports folder
function serveReports() {
  return {
    name: 'serve-reports',
    configureServer(server) {
      server.middlewares.use('/reports', express.static(path.resolve(__dirname, 'reports')));
    }
  };
}

export default defineConfig(() => {
  return {
    plugins: [react(), tailwindcss(), serveReports()],
    resolve: {
      alias: {
        '@': path.resolve(__dirname, '.'),
      },
    },
    server: {
      // HMR configuration
      hmr: process.env.DISABLE_HMR !== 'true',
      watch: process.env.DISABLE_HMR === 'true' ? null : {},
    },
  };
});
