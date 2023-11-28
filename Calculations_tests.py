import unittest
from Calculations import add, multiply, power

class ExampleTests(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(8, 2), 10, 'The sum is wrong.')

    def test_multiply(self):
        self.assertEqual(multiply(8, 2), 16, 'The multiplication is wrong.')

    def test_power(self):
        self.assertEqual(power(2, 4), 16, '2 to power of 4 result is wrong.')

if __name__ == '__main__':
    unittest.main()