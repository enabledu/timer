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