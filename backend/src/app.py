from fastapi import APIRouter
from fastapi.responses import RedirectResponse


app = APIRouter(tags=["timer"], prefix="/timer")


@app.get("/")
async def read_root():
    return RedirectResponse(url="http://127.0.0.1:8000/timer/frontend/out/index.html")

