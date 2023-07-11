from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class ErrorModel(BaseModel):
    detail: str


class Owner(BaseModel):
    id: UUID
    username: str
    email: str


class ProjectID(BaseModel):
    id: UUID


class TimeEntryID(BaseModel):
    id: UUID


class TimeEntryRead(BaseModel):
    id: UUID
    name: str
    project: ProjectID

    owner: Owner

    start_datetime: datetime
    # continue implementing


class TimeEntryUpdate(BaseModel):
    pass


class TimeEntryCreate(BaseModel):
    pass


class ProjectRead(BaseModel):
    pass


class ProjectUpdate(BaseModel):
    pass


class ProjectCreate(BaseModel):
    pass
