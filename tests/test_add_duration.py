from unittest import TestCase
from utils.time_calculator import add_duration

class TestAddDuration(TestCase):
    def test_am_start_time(self):
        result = add_duration('12:45 AM', '8:35')
        self.assertEqual(result, '9:20 AM')
    
    def test_pm_start_time(self):
        result = add_duration('8:24 PM', '9:01')
        self.assertEqual(result, '5:25 AM (next day)')
    
    def test_start_day_of_week_more_than_1_day(self):
        result = add_duration('12:00 AM', '61:23', 'Tuesday')
        self.assertEqual(result, '1:23 PM, Thursday (2 days later)')
        
    def test_no_start_day_of_week(self):
        result = add_duration('12:00 AM', '61:23')
        self.assertEqual(result, '1:23 PM (2 days later)')
    
    def test_case_insensitivity(self):
        result = add_duration('1:30 PM', '24:23', 'tHursdaY')
        self.assertEqual(result, '1:53 PM, Friday (next day)')
    
    def test_more_than_a_week_span(self):
        result = add_duration('2:20 PM', '632:23', 'Thursday')
        self.assertEqual(result, '10:43 PM, Tuesday (26 days later)')
        