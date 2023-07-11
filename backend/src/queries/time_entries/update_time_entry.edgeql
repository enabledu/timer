update Time_Entry
filter .id = <uuid>$time_entry_id
set {
  name := <str>$name,
  start_datetime := <datetime>$start_datetime,
  end_datetime := <datetime>$end_datetime,
}