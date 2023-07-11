from timer.backend.src.enums import WeekDays, Months


def get_day_name(dow: int) -> str:
    return WeekDays(dow).name


def get_month_name(month_number: int) -> str:
    return Months(month_number).name
