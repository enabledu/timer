from uuid import UUID

from edgedb import AsyncIOClient
from fastapi import Depends, HTTPException

from enabled.backend.src.database import get_client

from timer.backend.src import queries


async def get_project(project_id: UUID,
                      client: AsyncIOClient = Depends(get_client)):
    project = await queries.get_project(client, project_id=project_id)
    if not project:
        raise HTTPException(status_code=404, detail="PROJECT_NOT_FOUND")
    else:
        return project
    
    
async def get_time_entry(time_entry_id: UUID,
                         client: AsyncIOClient = Depends(get_client)):
    time_entry = await queries.get_time_entry(client, time_entry_id=time_entry_id)
    if not time_entry:
        raise HTTPException(status_code=404, detail="TIME_ENTRY_NOT_FOUND")
    else:
        return time_entry
