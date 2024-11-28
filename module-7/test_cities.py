# Alisa Steensen
# Module 7.2

# Test code for city_functions 

import unittest
from city_functions import city_country

class TestCityFunction(unittest.TestCase):
    """Tests for the city_functions.py"""

    def test_city_country(self):
        """Test if the function returns the correct format."""
        result = city_country("santiago", "chile")
        self.assertEqual(result, "Santiago, Chile")

        result = city_country("paris", "france")
        self.assertEqual(result, "Paris, France")

        result = city_country("tokyo", "japan")
        self.assertEqual(result, "Tokyo, Japan")

if __name__ == "__main__":
    unittest.main()
