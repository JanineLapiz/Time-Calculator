from enum import Enum
    
class Meridiem(Enum):
    AM = 'AM'
    PM = 'PM'

class DayOfWeek(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    
    @property
    def label(self) -> str:
        return self.name.lower().capitalize()