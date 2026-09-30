import mimetypes
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


BASE_DIR = Path(__file__).resolve().parent
mimetypes.add_type("image/webp", ".webp")

app = FastAPI(
    title="Red Impacto LATAM — réplica",
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)


@app.middleware("http")
async def security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "img-src 'self' data:; "
        "frame-src https://www.youtube-nocookie.com https://www.youtube.com https://iwxei6q3.insforge.site; "
        "script-src 'self' https://iwxei6q3.insforge.site; "
        "connect-src 'self' https://iwxei6q3.insforge.site; "
        "style-src 'self' https://iwxei6q3.insforge.site; font-src 'self'; "
        "object-src 'none'; base-uri 'self'; form-action 'self'; frame-ancestors 'none'"
    )
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"
    response.headers["X-Frame-Options"] = "DENY"
    return response


app.mount("/assets", StaticFiles(directory=BASE_DIR / "assets"), name="assets")


@app.get("/", include_in_schema=False)
def index() -> FileResponse:
    return FileResponse(BASE_DIR / "index.html", media_type="text/html")


@app.get("/styles.css", include_in_schema=False)
def styles() -> FileResponse:
    return FileResponse(BASE_DIR / "styles.css", media_type="text/css")


@app.get("/responsive.css", include_in_schema=False)
def responsive_styles() -> FileResponse:
    return FileResponse(BASE_DIR / "responsive.css", media_type="text/css")


@app.get("/script.js", include_in_schema=False)
def script() -> FileResponse:
    return FileResponse(BASE_DIR / "script.js", media_type="application/javascript")
