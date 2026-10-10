# Ticker Web App

A fullscreen, wide-display ticker designed to run locally on a Raspberry Pi 4. The project intentionally has separate frontend and backend directories, while FastAPI serves the frontend in production so the Pi only needs one process.

## What is included

- A fullscreen display with a clock, headline strip, market-style cards, and a scrolling ticker.
- A small JSON-backed API for the screen's content.
- A no-build frontend (plain HTML, CSS, and JavaScript) to keep the device footprint low.
- Responsive wide-screen styling; it looks best at 16:9, ultrawide, or other landscape displays.

## Project layout

```
backend/        Python/FastAPI API and content store
frontend/       Display application (HTML, CSS, JavaScript)
```

## Run locally

Requires Python 3.11 or newer.

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Open `http://localhost:8000`. On a Pi, open `http://localhost:8000` in Chromium's kiosk mode.

## Change the display content

Edit [ticker.json](backend/data/ticker.json), then refresh the browser. The API is also available at:

- `GET /api/ticker` — current screen data
- `PUT /api/ticker` — replace screen data (useful for a future admin interface)
- `GET /health` — service health check

The included content is sample data. Future integrations (weather, stocks, calendar, news) should fetch their source in the backend and return the same shape from `/api/ticker`; do not expose API keys to the frontend.

## Raspberry Pi notes

- Use Raspberry Pi OS 64-bit and wired Ethernet when practical.
- Start with a 1080p display; the layout scales to wider screens without changing JavaScript.
- For kiosk launch, Chromium supports: `chromium --kiosk --start-fullscreen http://localhost:8000`.
- Run Uvicorn under a `systemd` service for automatic restarts once the app moves to the Pi.

## Run with Docker

Docker Desktop on a Mac and Docker Engine on a 64-bit Raspberry Pi 4 can build this image directly. The official Python base image is multi-architecture, so Docker selects the appropriate image for the machine building it.

```bash
git clone https://github.com/YOUR-USERNAME/ticker-webapp.git
cd ticker-webapp
docker compose up --build -d
```

The display is then available at `http://localhost:8000` on the Pi. The Compose file mounts `backend/data` into the container, so edits to `backend/data/ticker.json` persist across rebuilds and restarts.

Useful commands:

```bash
docker compose logs -f
docker compose down
docker compose up --build -d
```

To update the app after pushing a new version to GitHub:

```bash
git pull
docker compose up --build -d
```
