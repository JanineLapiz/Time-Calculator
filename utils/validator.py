import re

def validate_start_time(start_time: str) -> None:
    start_time_pattern = r'\d{1,2}:\d{2} [AP]M'
        
    if not re.match(start_time_pattern, start_time): raise Exception('Invalid start time pattern')
    
    hours_and_minutes = start_time.split()[0]
    
    [hours, minutes] = hours_and_minutes.split(':')
    
    if int(hours) > 12 or int(hours) < 1: raise Exception('Must be a 12-hour format')
        
    # No need to check if minutes is less than 0. 
    # The pattern check above ensures it's always an integer.
    if int(minutes) >= 60: raise Exception('Invalid minutes')
    

def validate_duration(duration: str) -> None:
    duration_pattern = r'\d+:\d{2}'
    
    if not re.match(duration_pattern, duration): raise Exception('Invalid duration format')
    
    minutes = duration.split(':')[1]
    
    # No need to check if minutes is less than 0. 
    # The pattern check above ensures it's always an integer.
    if int(minutes) >= 60: raise Exception('Invalid minutes')
    

def is_minutes(minutes: int) -> bool:
    if minutes >= 60: return False
    if minutes < 0: return False
    return True