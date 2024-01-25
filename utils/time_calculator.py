from models.constants import DayOfWeek
from models.Time import Parsed24HourFormat
from utils.parser import parse_duration, parse_start_time, parse_start_day_of_week
from utils.time_converter import to_parsed_12_hour_format, to_parsed_24_hour_format
from utils.formatter import format_date_time

def add_days_to_day_of_week(start_day_of_week: DayOfWeek | None, days: int) -> DayOfWeek | None:
    if not start_day_of_week: return None
    
    end_day_of_week_number = (start_day_of_week.value + days) % 7
    end_day_of_week = DayOfWeek(end_day_of_week_number)
    
    return end_day_of_week


def add_duration(_start_time: str, _duration: str, _start_day_of_week: str | None = None):
    start_time_parsed_24_hour = to_parsed_24_hour_format(
        parse_start_time(_start_time)
    )
    duration = parse_duration(_duration)
    start_day_of_week = parse_start_day_of_week(_start_day_of_week)
    
    # Use `//` and`%`` instead of `divmod()` to increase readability
    total_minutes = start_time_parsed_24_hour.minutes + duration.minutes
    total_hours = start_time_parsed_24_hour.hours + duration.hours + (total_minutes // 60)
    total_days =  total_hours // 24
 
    end_time = to_parsed_12_hour_format(
        Parsed24HourFormat(total_hours % 24, total_minutes % 60)
    )
    end_day_of_week = add_days_to_day_of_week(start_day_of_week, total_days)
    
    formatted_end_date_time = format_date_time(end_time, end_day_of_week)
    
    if total_days < 1: 
        return formatted_end_date_time
    
    if total_days < 2:
        return f'{formatted_end_date_time} (next day)'
    
    return f'{formatted_end_date_time} ({total_days} days later)'