import json

import unittest

from hello_world import app




def lambda_handler(event, context):
    number1 = event['Number1']
    number2 = event['Number2']
    def sum():
        return number1 + number2
    def product():
        return number1 * number2
    def difference():
        return abs(number1 - number2)
    def quotient():
        return number1 / number2

class TestSum(unittest.TestCase):

    def test_add(self):
        self.assertEqual(sum([2,2]), 4, "Should be 4")
    def test_product(self):
        self.assertEqual(product([3, 2]), 6, "Should be 6")
    def test_sub(self):
        self.assertEqual(difference([4, 1]), 3, "Should be 3")
    def test_division(self):
        self.assertEqual(quotient([4,2]), 2, "Should be 2")

if __name__ == '__main__':
    unittest.main()
