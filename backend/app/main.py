from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .models import TickerContent
from .store import read_content, write_content


PROJECT_ROOT = Path(__file__).resolve().parents[2]
FRONTEND_DIR = PROJECT_ROOT / "frontend"

app = FastAPI(title="Ticker API", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/ticker", response_model=TickerContent)
def get_ticker() -> TickerContent:
    try:
        return read_content()
    except (OSError, ValueError) as error:
        raise HTTPException(status_code=500, detail="Ticker content is unavailable") from error


@app.put("/api/ticker", response_model=TickerContent)
def update_ticker(content: TickerContent) -> TickerContent:
    try:
        return write_content(content)
    except OSError as error:
        raise HTTPException(status_code=500, detail="Ticker content could not be saved") from error


@app.get("/")
def display() -> FileResponse:
    return FileResponse(FRONTEND_DIR / "index.html")


app.mount("/assets", StaticFiles(directory=FRONTEND_DIR), name="frontend-assets")
