module default {
    type Project {
        required property name -> str;
        multi link time_entries -> Time_Entry {
            on target delete allow;
            on source delete delete target;
        }
    }

    type Time_Entry {
        required link owner -> User;

        required property name -> str;

        link project := (select .<time_entries[is Project] limit 1);

        required property start_datetime -> datetime;
        property day_s := (datetime_get(.start_datetime, 'day'));
        property dow_s := (datetime_get(.start_datetime, 'dow'));
        property month_s := (datetime_get(.start_datetime, 'month'));
        property year_s := (datetime_get(.start_datetime, 'year'));

        required property end_datetime -> datetime;
        property day_e := (datetime_get(.end_datetime, 'day'));
        property dow_e := (datetime_get(.end_datetime, 'dow'));
        property month_e := (datetime_get(.end_datetime, 'month'));
        property year_e := (datetime_get(.end_datetime, 'year'));

        property duration := (.end_datetime - .start_datetime);
        property hours_d := (duration_get(.duration, 'hour'));
        property minutes_d := (duration_get(.duration, 'minutes'));
        property seconds_d := (duration_get(.duration, 'seconds'));
    }
}