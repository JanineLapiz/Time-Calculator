from utils.validator import validate_time
from enum import Enum

class Time:
    def __init__(self, time: str):
        validate_time(time)
        
        [hours_and_minutes, meridiem] = time.split()
        [hours, minutes] = hours_and_minutes.split(':')
        
        self.time_12_hour = Time12Hour(int(hours), int(minutes), meridiem)
    
    @property
    def time_24_hour(self):
        hours = self.time_12_hour.hours
        minutes = self.time_12_hour.minutes
        meridiem = self.time_12_hour.meridiem
        
        if hours == 12 and meridiem == Meridiem.AM: 
            return Time24Hour(00, minutes)
        
        if meridiem == Meridiem.AM:
            return Time24Hour(hours, minutes)

        if hours == 12: 
            return Time24Hour(hours, minutes)
        
        return Time24Hour(hours + 12, minutes)


class Meridiem(Enum):
    AM = 'AM'
    PM = 'PM'


class Time12Hour:
    hours: int
    minutes: int
    meridiem: Meridiem
    
    def __init__(self, hours: int, minutes: int, meridiem: Meridiem):
        self.hours = hours
        self.minutes = minutes
        
        match meridiem:
            case Meridiem.AM.value: 
                self.meridiem = Meridiem.AM
            case Meridiem.PM.value:
                self.meridiem = Meridiem.PM
            case _:
                raise Exception('Invalid meridiem value.')
        

class Time24Hour:
    def __init__(self, hours: int, minutes: int):
        self.hours = hours
        self.minutes = minutes
        