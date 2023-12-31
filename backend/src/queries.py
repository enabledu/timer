import datetime
import edgedb
import uuid


async def add_time_entry(
    executor: edgedb.AsyncIOExecutor,
    *,
    owner_id: uuid.UUID,
    start_datetime: datetime.datetime,
    end_datetime: datetime.datetime,
    project_id: uuid.UUID,
    name: str
):
    return await executor.query_single(
        """\
        with
          owner := (
            select User
            filter .id = <uuid>$owner_id
          ),
          time_entry := (
            insert Time_Entry {
              name := <str>$name,
              start_datetime := <datetime>$start_datetime,
              end_datetime := <datetime>$end_datetime,
              owner := owner
            }
          ),
          project := (
            update Project
            filter .id = <optional uuid>$project_id
            set {
              time_entries += time_entry
            }
          )
        select time_entry
        """,
        owner_id=owner_id,
        start_datetime=start_datetime,
        end_datetime=end_datetime,
        project_id=project_id,
        name=name
    )


async def create_project(
    executor: edgedb.AsyncIOExecutor,
    *,
    project_name: str,
):
    return await executor.query_single(
        """\
        insert Project {
          name := <str>$project_name,
        }
        """,
        project_name=project_name,
    )


async def delete_project(
    executor: edgedb.AsyncIOExecutor,
    *,
    project_id: uuid.UUID,
):
    return await executor.query_single(
        """\
        delete Project
        filter .id = <uuid>$project_id\
        """,
        project_id=project_id,
    )


async def delete_time_entry(
    executor: edgedb.AsyncIOExecutor,
    *,
    time_entry_id: uuid.UUID,
):
    return await executor.query_single(
        """\
        delete Time_Entry
        filter .id = <uuid>$time_entry_id\
        """,
        time_entry_id=time_entry_id,
    )


async def get_all_projects(
    executor: edgedb.AsyncIOExecutor,
):
    return await executor.query(
        """\
        select Project {
          id,
          name,
        
          time_entries: {
            id,
            name,
            
            owner: {
              id,
              username,
              email
            },
        
            start_datetime,
            day_s,
            dow_s,
            month_s,
            year_s,
        
            end_datetime,
            day_e,
            dow_e,
            month_e,
            year_e,
        
            duration,
            hours_d,
            minutes_d,
            seconds_d
          }
        }
        """,
    )


async def get_all_project_time_entries(
    executor: edgedb.AsyncIOExecutor,
):
    return await executor.query(
        """\
        with project := (
          select Project
          filter .id = <uuid>$project_id
        )
        select project.time_entries {
          id,
          name,
          
          owner: {
            id,
            username,
            email
          },
        
          start_datetime,
          day_s,
          dow_s,
          month_s,
          year_s,
        
          end_datetime,
          day_e,
          dow_e,
          month_e,
          year_e,
        
          duration,
          hours_d,
          minutes_d,
          seconds_d
        }
        """,
    )


async def get_all_time_entries(
    executor: edgedb.AsyncIOExecutor,
):
    return await executor.query(
        """\
        select Time_Entry {
          id,
          name,
          project,
        
          user := (.owner.username),
          email := (.owner.email),
        
          start_datetime,
          day_s,
          dow_s,
          month_s,
          year_s,
        
          end_datetime,
          day_e,
          dow_e,
          month_e,
          year_e,
        
          duration,
          hours_d,
          minutes_d,
          seconds_d
        } filter exists .end_datetime
        """,
    )


async def get_project(
    executor: edgedb.AsyncIOExecutor,
    *,
    project_id: uuid.UUID,
):
    return await executor.query_single(
        """\
        select Project {
          id,
          name,
        
          time_entries: {
            id,
            name,
            
            owner: {
              id,
              username,
              email
            },
        
            start_datetime,
            day_s,
            dow_s,
            month_s,
            year_s,
        
            end_datetime,
            day_e,
            dow_e,
            month_e,
            year_e,
        
            duration,
            hours_d,
            minutes_d,
            seconds_d
          }
        } filter .id = <uuid>$project_id
        """,
        project_id=project_id,
    )


async def get_time_entry(
    executor: edgedb.AsyncIOExecutor,
    *,
    time_entry_id: uuid.UUID,
):
    return await executor.query_single(
        """\
        select Time_Entry {
          id,
          name,
          project,
        
          owner: {
            id,
            username,
            email
          },
        
          start_datetime,
          day_s,
          dow_s,
          month_s,
          year_s,
        
          end_datetime,
          day_e,
          dow_e,
          month_e,
          year_e,
        
          duration,
          hours_d,
          minutes_d,
          seconds_d
        } filter .id = <uuid>$time_entry_id
        """,
        time_entry_id=time_entry_id,
    )


async def update_project(
    executor: edgedb.AsyncIOExecutor,
    *,
    project_id: uuid.UUID,
    name: str,
):
    return await executor.query_single(
        """\
        update Project
        filter .id = <uuid>$project_id
        set {
          name := <str>$name
        }\
        """,
        project_id=project_id,
        name=name,
    )


async def update_time_entry(
    executor: edgedb.AsyncIOExecutor,
    *,
    time_entry_id: uuid.UUID,
    start_datetime: datetime.datetime,
    end_datetime: datetime.datetime,
    name: str,
):
    return await executor.query_single(
        """\
        update Time_Entry
        filter .id = <uuid>$time_entry_id
        set {
          name := <str>$name,
          start_datetime := <datetime>$start_datetime,
          end_datetime := <datetime>$end_datetime,
        }
        """,
        time_entry_id=time_entry_id,
        start_datetime=start_datetime,
        end_datetime=end_datetime,
        name=name,
    )
