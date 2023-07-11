from fastapi import APIRouter

from timer.backend.src.routers.projects import projects_router

from timer.backend.src.routers.entries import entries_router

app = APIRouter(prefix="/timer")

app.include_router(projects_router)
app.include_router(entries_router)
