import unittest
from task5 import convert_date_format
class TestConvertDateFormat(unittest.TestCase):
    def test_valid_date(self):
        self.assertEqual(convert_date_format("2023-10-15"), "15-10-2023")
        self.assertEqual(convert_date_format("1999-01-01"), "01-01-1999")
    def test_invalid_format_missing_parts(self):
        self.assertEqual(convert_date_format("2023-10"), "Invalid format")
        self.assertEqual(convert_date_format("2023"), "Invalid format")
    def test_invalid_format_extra_parts(self):
        self.assertEqual(convert_date_format("2023-10-15-01"), "Invalid format")
    def test_empty_string(self):
        self.assertEqual(convert_date_format(""), "Invalid format")
    def test_non_numeric_input(self):
        self.assertEqual(convert_date_format("year-month-day"), "Invalid format")
    def test_leading_zeros(self):
        self.assertEqual(convert_date_format("2023-07-09"), "09-07-2023")
    def test_single_digit_day_month(self):
        self.assertEqual(convert_date_format("2023-7-9"), "9-7-2023")
if __name__ == "__main__":
    unittest.main()