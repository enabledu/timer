from uuid import UUID

from edgedb import AsyncIOClient
from fastapi import APIRouter, Depends, Body
from enabled.backend.src.database import get_client

from timer.backend.src.dependencies import get_project as get_project_dependency
from timer.backend.src import queries

from timer.backend.src.models import ErrorModel

projects_router = APIRouter(tags=["timer: projects"], prefix="/projects")


@projects_router.get("/")
async def get_all_projects(client: AsyncIOClient = Depends(get_client)):
    return await queries.get_all_projects(client)


@projects_router.get("/{project_id}/",
                     responses={404: {"model": ErrorModel}})
async def get_project(project=Depends(get_project_dependency)):
    return project


@projects_router.post("/create/")
async def create_project(project_name: str = Body(),
                         client: AsyncIOClient = Depends(get_client)):
    return await queries.create_project(client, project_name=project_name)


@projects_router.post("/{project_id}/edit/",
                      dependencies=[Depends(get_project)],
                      responses={404: {"model": ErrorModel}})
async def edit_project(project_id: UUID,
                       name: str = Body(),
                       client: AsyncIOClient = Depends(get_client)):
    return await queries.update_project(client, project_id=project_id, name=name)


@projects_router.delete("/{project_id}/",
                        dependencies=[Depends(get_project)],
                        responses={404: {"model": ErrorModel}})
async def delete_project(project_id: UUID,
                         client: AsyncIOClient = Depends(get_client)):
    return await queries.delete_project(client, project_id=project_id)
