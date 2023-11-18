from models.Time import Parsed24HourFormat, Parsed12HourFormat
from models.constants import Meridiem

def to_parsed_12_hour_format(time: Parsed24HourFormat) -> Parsed12HourFormat:
    hours = time.hours
    minutes = time.minutes
            
    if hours == 0: return Parsed12HourFormat(12, minutes, Meridiem.AM)

    if hours <= 12: return Parsed12HourFormat(hours, minutes, Meridiem.AM)
    
    return Parsed12HourFormat(hours - 12, minutes, Meridiem.PM)


def to_parsed_24_hour_format(time: Parsed12HourFormat) -> Parsed24HourFormat:
    hours = time.hours
    minutes = time.minutes
    meridiem = time.meridiem
    
    if hours == 12 and meridiem == Meridiem.AM:
        return Parsed24HourFormat(00, minutes)

    if meridiem == Meridiem.AM or (hours == 12 and meridiem == Meridiem.PM):
        return Parsed24HourFormat(hours, minutes)
        
    return Parsed24HourFormat(hours + 12, minutes)