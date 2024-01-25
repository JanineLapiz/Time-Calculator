from models.constants import Meridiem
from utils.validator import is_minutes

class Parsed12HourFormat:    
    def __init__(self, hours: int, minutes: int, meridiem: Meridiem):
        if hours > 12 or hours < 0: 
            raise Exception('Cannot parse 12-hour format. Invalid hours.')
        
        if not is_minutes(minutes):
            raise Exception('Cannot parse 12-hour format. Invalid minutes.')
        
        self.hours = hours
        self.minutes = minutes
        self.meridiem = meridiem
    
    @property
    def formatted_string(self) -> str:
        return f'{self.hours}:{self.minutes} {self.meridiem.name}'
        

class Parsed24HourFormat:
    def __init__(self, hours: int, minutes: int):
        if hours >= 24 or hours < 0:
            raise Exception('Cannot parse 24-hour format. Invalid hours.')
        
        if not is_minutes(minutes):
            raise Exception('Cannot parse 24-hour format. Invalid minutes.')
        
        self.hours = hours
        self.minutes = minutes
        
    @property
    def formatted_string(self) -> str:
        return f'{self.hours}:{self.minutes}'


class Duration:
    def __init__(self, hours: int, minutes: int): 
        if not is_minutes(minutes):
            raise Exception('Cannot parse duration. Invalid minutes.')
                       
        self.hours = hours
        self.minutes = minutes
        
    @property
    def formatted_string(self) -> str:
        return f'{self.hours}:{self.minutes}'