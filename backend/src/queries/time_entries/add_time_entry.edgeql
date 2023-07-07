with
  owner := (
    select User
    filter .id = <uuid>$owner_id
  ),
  time_entry := (
    insert Time_Entry {
      start_datetime := <datetime>$start_datetime,
      owner := owner
    }
  ),
  project := (
    update Project
    filter .id = <uuid>$project_id
    set {
      time_entries += time_entry
    }
  )
select time_entry