from solutions import seconds_to_hours_minutes_seconds

import unittest
import random

class TestSecondsToHoursMinutesSeconds(unittest.TestCase):
    def test_0(self):
        sec = 0
        
        expected = "00:00:00"
        actual = seconds_to_hours_minutes_seconds(sec)

        self.assertEqual(expected, actual)

    def test_60(self):
        sec = 60
        
        expected = "00:01:00"
        actual = seconds_to_hours_minutes_seconds(sec)

        self.assertEqual(expected, actual)

    def test_3600(self):
        sec = 3600
        
        expected = "01:00:00"
        actual = seconds_to_hours_minutes_seconds(sec)

        self.assertEqual(expected, actual)

    def test_random(self):
        for _ in range(10000):
            h = random.randint(0, 23)
            m = random.randint(0, 59)
            s = random.randint(0, 59)

            expected = "%02d:%02d:%02d" % (h, m, s)
            actual = seconds_to_hours_minutes_seconds(h * 60 * 60 + m * 60 + s)

            self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
