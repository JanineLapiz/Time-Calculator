from unittest import TestCase
from utils.parser import parse_start_time
from models.constants import Meridiem

class TestStartTimeParser(TestCase):
    def test_valid_time_12_am(self):
        parsed_start_time = parse_start_time('12:43 AM')
        
        self.assertEqual(parsed_start_time.hours, 12)
        self.assertEqual(parsed_start_time.minutes, 43)
        self.assertEqual(parsed_start_time.meridiem, Meridiem.AM)    
    
    def test_valid_time_12_pm(self):
        parsed_start_time = parse_start_time('12:55 PM')
        
        self.assertEqual(parsed_start_time.hours, 12)
        self.assertEqual(parsed_start_time.minutes, 55)
        self.assertEqual(parsed_start_time.meridiem, Meridiem.PM)
    
    def test_valid_time_am(self):
        parsed_start_time = parse_start_time('2:22 AM')
        
        self.assertEqual(parsed_start_time.hours, 2)
        self.assertEqual(parsed_start_time.minutes, 22)
        self.assertEqual(parsed_start_time.meridiem, Meridiem.AM)

    def test_valid_time_pm(self):
        parsed_start_time = parse_start_time('11:46 PM')
        
        self.assertEqual(parsed_start_time.hours, 11)
        self.assertEqual(parsed_start_time.minutes, 46)
        self.assertEqual(parsed_start_time.meridiem, Meridiem.PM)

    def test_validation_in_time_parser(self):
        with self.assertRaises(Exception) as context:
            parse_start_time('1sd:23 p,')
            
        self.assertEqual(str(context.exception), 'Invalid start time pattern')