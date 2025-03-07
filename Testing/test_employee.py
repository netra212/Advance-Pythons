import unittest
from unittest.mock import patch
from employee import Employee

'''
Mocking in Python is a technique used in unit testing to replace real objects with mock objects that simulate their behavior. This allows you to test components in isolation without relying on external dependencies such as databases, APIs, or file systems.

#. Why Use Mocking?
-> Isolate components: Ensures tests focus only on the specific functionality being tested.
-> Avoid side effects: Prevents interactions with external systems like databases or APIs.
-> Control return values: Allows setting expected responses for function calls.
-> Simulate exceptions: Helps test how the code handles errors.

# Python's unittest.mock module provides tools for mocking.

# 1. Using MagicMock.
-> MagicMock is a powerful mock object that automatically generates return values.

----------------------------------------------------
from unittest.mock import MagicMock

# Create a mock object
mock_obj = MagicMock()

# Set return value
mock_obj.some_method.return_value = "Hello, Mock!"

# Call the method
print(mock_obj.some_method())  # Output: Hello, Mock!
----------------------------------------------------

# 2. 
'''
class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")
    
    @classmethod
    def classmethod(cls):
        print("teardownClass")

    # Run before every single test. 
    def setUp(self):
        print("\nsetUp")
        self.emp_1 = Employee("Corey", "Schafer", 50000)
        self.emp_2 = Employee("Sue", "Smith", 60000)
    
    # Run at the end of the code. 
    def tearDown(self):
        pass

    def test_email(self):
        print('\ntest_email')
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):

        print('\ntest_fullname')

        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        print('\ntest_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch("employee.requests.get") as mocked_get:
            mocked_get.return_value.ok == True
            mocked_get.return_value.text = "Success"

            schedule = self.emp_1.monthly_schedule("May")
            mocked_get.assert_called_with("http://company.com/Schafer/May")
            self.assertEqual(schedule, "Success")

            mocked_get.return_value.ok == False

            schedule = self.emp_2.monthly_schedule("June")
            mocked_get.assert_called_with("http://company.com/Smith/June")
            self.assertEqual(schedule, "Bad Response!")

if __name__ == '__main__':
    unittest.main()