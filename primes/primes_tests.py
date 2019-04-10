import unittest
import primes

class TestPrimes(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(primes.is_prime(3))
        self.assertFalse(primes.is_prime(4))
        self.assertTrue(primes.is_prime(13))
    
    def test_get_primes(self):
        fifth_prime = primes.get_primes(5)
        self.assertEqual(fifth_prime[-1], 9)
        ten_primes = primes.get_primes(10)
        self.assertEqual(10, len(ten_primes))

if __name__=="__main__":
    unittest.main()
