module default {
    type Project {
        required property name -> str;
        required link owner -> User;
        multi link time_entries -> Time_Entry;
    }

    type Time_Entry {
        required property start_datetime -> datetime;
        property day_s := (datetime_get(.start_datetime, 'day'));
        property dow_s := (datetime_get(.start_datetime, 'dow'));
        property month_s := (datetime_get(.start_datetime, 'month'));
        property year_s := (datetime_get(.start_datetime, 'year'));

        property end_datetime -> datetime;
        property day_e := (datetime_get(.end_datetime, 'day'));
        property dow_e := (datetime_get(.end_datetime, 'dow'));
        property month_e := (datetime_get(.end_datetime, 'month'));
        property year_e := (datetime_get(.end_datetime, 'year'));

        property duration := (.start_datetime - .end_datetime);
        property hours_d := (duration_get(.duration, 'hour'));
        property minutes_d := (duration_get(.duration, 'minutes'));
        property seconds_d := (duration_get(.duration, 'seconds'));
    }
}