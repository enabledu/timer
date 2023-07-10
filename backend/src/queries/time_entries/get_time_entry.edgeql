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
} filter .id = <uuid>$time_entry