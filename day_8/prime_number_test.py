import unittest
import prime_number

class MyTestCase(unittest.TestCase):
    def test_prime_number_func(self):
        result = prime_number.prime_checker(13)
        self.assertEqual(result, "It's a prime number.")
    def test_prime_number_func_2(self):
        result = prime_number.prime_checker(7)
        self.assertEqual(result, "It's a prime number.")
    def test_prime_number_func_3(self):
        result = prime_number.prime_checker(8)
        self.assertEqual(result, "It's not a prime number.")
    def test_prime_number_func_4(self):
        result = prime_number.prime_checker(59)
        self.assertEqual(result, "It's a prime number.")
    def test_prime_number_func_5(self):
        result = prime_number.prime_checker(78)
        self.assertEqual(result, "It's not a prime number.")