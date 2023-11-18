from models.Time import Parsed12HourFormat, Duration
from utils.validator import validate_start_time, validate_duration
from models.constants import Meridiem, DayOfWeek

def parse_start_time(start_time: str) -> Parsed12HourFormat:
    validate_start_time(start_time)
        
    [hours_and_minutes, meridiem] = start_time.split()
    [hours, minutes] = hours_and_minutes.split(':')
    
    return  Parsed12HourFormat(
        int(hours), 
        int(minutes), 
        Meridiem(meridiem.upper())
    )
    

def parse_duration(duration: str) -> Duration:
    validate_duration(duration)
    
    [hours, minutes] = duration.split(':')
    
    return Duration(
        int(hours),
        int(minutes)
    )
    
def parse_start_day_of_week(start_day_of_week: str | None) -> DayOfWeek | None:
    if not start_day_of_week: return None
    return DayOfWeek(start_day_of_week.upper())