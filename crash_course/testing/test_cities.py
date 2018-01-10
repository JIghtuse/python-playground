import unittest
from city_functions import make_formatted_name

class CityTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Do names like 'Santiago, Chile' work?"""
        formatted_name = make_formatted_name('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do names like 'Santiago, Chile - population 500' work?"""
        formatted_name = make_formatted_name('santiago', 'chile', 5000000)
        self.assertEqual(formatted_name, 'Santiago, Chile - population 5000000')

unittest.main()
