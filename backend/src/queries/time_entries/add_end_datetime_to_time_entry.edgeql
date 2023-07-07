update Time_Entry
filter .id = <uuid>$time_entry_id
set {
  end_datetime := <datetime>$end_datetime
}