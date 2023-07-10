import dataclasses
from enum import Enum

from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from timer.backend.src import queries
from enabled.backend.src.database import get_client


app = APIRouter(tags=["timer"], prefix="/timer")


@app.get("/")
async def read_root():
    return RedirectResponse(url="http://127.0.0.1:8000/timer/frontend/out/index.html")


class WeekDays(Enum):
    Sunday = 0
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6


class Months(Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12


def get_day_name(dow: int) -> str:
    return WeekDays(dow).name


def get_month_name(month_number: int) -> str:
    return Months(month_number).name


@app.get("/entries/")
async def get_all_time_entries(client=Depends(get_client)):
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
