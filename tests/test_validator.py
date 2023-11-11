from unittest import TestCase
from utils.validator import validate_duration, validate_start_time

class TestValidateStartTime(TestCase):
    def test_time_is_valid(self):
        self.assertIsNone(validate_start_time('12:30 AM'))
        self.assertIsNone(validate_start_time('2:30 AM'))
        self.assertIsNone(validate_start_time('2:30 PM'))
        
    def test_no_meridiem(self):
        with self.assertRaises(Exception) as context:
            validate_start_time('12:00')
        self.assertEqual(str(context.exception), 'Invalid start time pattern')
    
    def test_meridiem_is_invalid(self):
        with self.assertRaises(Exception) as context:
            validate_start_time('12:00 AA')
        self.assertEqual(str(context.exception), 'Invalid start time pattern')
        
    def test_no_minutes(self):
        with self.assertRaises(Exception) as context:
            validate_start_time('12 PM')
        self.assertEqual(str(context.exception), 'Invalid start time pattern')
        
    def test_minutes_is_letters(self):
        with self.assertRaises(Exception) as context:
            validate_start_time('12:fsdfsd AM')
        self.assertEqual(str(context.exception), 'Invalid start time pattern') 
        
    def test_minutes_is_more_than_2_digits(self):
        with self.assertRaises(Exception) as context:
            validate_start_time('4:450 PM')
        self.assertEqual(str(context.exception), 'Invalid start time pattern')
    
    def test_minutes_is_less_than_2_digits(self):
        with self.assertRaises(Exception) as context:
            validate_start_time('12:0 PM')
        self.assertEqual(str(context.exception), 'Invalid start time pattern')
    
    def test_minutes_is_more_than_60(self):
        with self.assertRaises(Exception) as context:
            validate_start_time('12:63 PM')
        self.assertEqual(str(context.exception), 'Invalid minutes')
            
    def test_minutes_is_less_than_0(self):
        with self.assertRaises(Exception) as context:
            validate_start_time('12:-50 PM')
        self.assertEqual(str(context.exception), 'Invalid start time pattern')

    def test_hours_is_letters(self):
        with self.assertRaises(Exception) as context:
            validate_start_time('sdfs:30 PM')
        self.assertEqual(str(context.exception), 'Invalid start time pattern')
    
    def test_hours_is_more_than_3_digits(self):
        with self.assertRaises(Exception) as context:
            validate_start_time('124:30 PM')
        self.assertEqual(str(context.exception), 'Invalid start time pattern')
    
    def test_hours_is_more_than_12(self):
        with self.assertRaises(Exception) as context:
            validate_start_time('13:00 AM') 
        self.assertEqual(str(context.exception), 'Must be a 12-hour format')
        
    def test_hours_is_less_than_1(self):
        with self.assertRaises(Exception) as context_b:
            validate_start_time('0:00 PM')
        self.assertEqual(str(context_b.exception), 'Must be a 12-hour format')
    
    
class TestValidateDuration(TestCase):
    def test_duration_is_valid(self):
        self.assertIsNone(validate_duration('1:30'))
        self.assertIsNone(validate_duration('235:00'))
        self.assertIsNone(validate_duration('0:10'))
    
    def test_hours_or_minutes_is_missing(self):
        with self.assertRaises(Exception) as context:
            validate_duration('234')
        self.assertEqual(str(context.exception), 'Invalid duration format')
    
    def test_minutes_is_less_than_2_digits(self):
        with self.assertRaises(Exception) as context:
            validate_duration('12:1')
        self.assertEqual(str(context.exception), 'Invalid duration format')
        
    def test_minutes_is_more_than_60(self):
        with self.assertRaises(Exception) as context:
            validate_duration('12:80')
        self.assertEqual(str(context.exception), 'Invalid minutes')
    
    def test_minutes_is_less_than_0(self):
        with self.assertRaises(Exception) as context:
            validate_duration('12:-2')
        self.assertEqual(str(context.exception), 'Invalid duration format')
    
    def test_hours_is_less_than_0(self):
        with self.assertRaises(Exception) as context:
            validate_duration('-23:00')
        self.assertEqual(str(context.exception), 'Invalid duration format')