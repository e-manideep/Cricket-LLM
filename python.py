import unittest
from prime_factors import prime_factors

class TestPrimeFactors(unittest.TestCase):
    def test_input_1(self):
        self.assertEqual(prime_factors(1), [])
    
if __name__ == '__main__':
    unittest.main()
