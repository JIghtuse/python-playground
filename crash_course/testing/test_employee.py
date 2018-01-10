import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""

    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        self.employee = Employee('john', 'reese', 10000)

    def test_give_default_raise(self):
        """Test that giving default raise increase salary properly."""
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 10000 + 5000)

    def test_give_custom_raise(self):
        """Test that giving custom raise increase salary properly."""
        self.employee.give_raise(100)
        self.assertEqual(self.employee.salary, 10000 + 100)

unittest.main()
