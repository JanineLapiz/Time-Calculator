from unittest import TestCase
from utils.Time import Time, Meridiem

class TestValidateTimeUtils(TestCase):
    def test_valid_time_12_am(self):
        time = Time('12:43 AM')
        
        self.assertEqual(time.time_12_hour.hours, 12)
        self.assertEqual(time.time_12_hour.minutes, 43)
        self.assertEqual(time.time_12_hour.meridiem, Meridiem.AM)
        
        self.assertEqual(time.time_24_hour.hours, 00)
        self.assertEqual(time.time_24_hour.minutes, 43)
    
    
    def test_valid_time_12_pm(self):
        time = Time('12:55 PM')
        
        self.assertEqual(time.time_12_hour.hours, 12)
        self.assertEqual(time.time_12_hour.minutes, 55)
        self.assertEqual(time.time_12_hour.meridiem, Meridiem.PM)
        
        self.assertEqual(time.time_24_hour.hours, 12)
        self.assertEqual(time.time_24_hour.minutes, 55)
        
    
    def test_valid_time_am(self):
        time = Time('2:22 AM')
        
        self.assertEqual(time.time_12_hour.hours, 2)
        self.assertEqual(time.time_12_hour.minutes, 22)
        self.assertEqual(time.time_12_hour.meridiem, Meridiem.AM)
        
        self.assertEqual(time.time_24_hour.hours, 2)
        self.assertEqual(time.time_24_hour.minutes, 22)
        
    def test_valid_time_pm(self):
        time = Time('11:46 PM')
        
        self.assertEqual(time.time_12_hour.hours, 11)
        self.assertEqual(time.time_12_hour.minutes, 46)
        self.assertEqual(time.time_12_hour.meridiem, Meridiem.PM)
        
        self.assertEqual(time.time_24_hour.hours, 23)
        self.assertEqual(time.time_24_hour.minutes, 46)
        
    def test_validation_in_time_parser(self):
        with self.assertRaises(Exception) as context:
            Time('1sd:23 p,')
            
        self.assertEqual(str(context.exception), 'Invalid time pattern')