import dataclasses
from datetime import datetime
from uuid import UUID

from edgedb import AsyncIOClient
from fastapi import APIRouter, Depends, Body

from enabled.backend.src.database import get_client
from timer.backend.src.utils import get_day_name, get_month_name
from timer.backend.src import queries
from timer.backend.src.dependencies import get_time_entry as get_time_entry_dependency
from timer.backend.src.models import ErrorModel

from enabled.backend.src.users.users import current_active_user

entries_router = APIRouter(tags=["timer: entries"], prefix="/entries")


@entries_router.get("/")
async def get_all_time_entries(client: AsyncIOClient = Depends(get_client)):
    entries = await queries.get_all_time_entries(client)
    updated_entries = []
    for entry in entries:
        entry_dict = dataclasses.asdict(entry)
        entry_dict['day_name_s'] = get_day_name(entry_dict['dow_s'])
        entry_dict['day_name_e'] = get_day_name(entry_dict['dow_e'])
        entry_dict['month_name_s'] = get_month_name(entry_dict['month_s'])
        entry_dict['month_name_e'] = get_month_name(entry_dict['month_e'])
        updated_entries.append(entry_dict)
    return updated_entries


@entries_router.get("/{time_entry_id}/",
                    responses={404: {"model": ErrorModel}})
async def get_time_entry(time_entry=Depends(get_time_entry_dependency)):
    return time_entry


@entries_router.post("/create/")
async def create_time_entry(name: str = Body(),
                            start_datetime: datetime = Body(),
                            end_datetime: datetime = Body(),
                            project_id: UUID = Body(None),
                            user=Depends(current_active_user),
                            client: AsyncIOClient = Depends(get_client)):
    return await queries.add_time_entry(client,
                                        name=name,
                                        owner_id=user.id,
                                        start_datetime=start_datetime,
                                        end_datetime=end_datetime,
                                        project_id=project_id)


# TODO: implement the update_time_entry endpoint


@entries_router.delete("/{time_entry_id}/",
                       dependencies=[Depends(get_time_entry)],
                       responses={404: {"model": ErrorModel}})
async def delete_time_entry(time_entry_id: UUID,
                            client: AsyncIOClient = Depends(get_client)):
    return await queries.delete_time_entry(client, time_entry_id=time_entry_id)
