from models.Time import Parsed12HourFormat
from models.constants import DayOfWeek

def format_date_time(time: Parsed12HourFormat, day_of_week: DayOfWeek | None) -> str:
    if not day_of_week:
        return time.formatted_string

    return ', '.join([time.formatted_string, day_of_week.label])