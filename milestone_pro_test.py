import unittest
from milestone_pro import *

class TestMymethodsMethods(unittest.TestCase):


  def test_print_board(self):
      self.assertTrue(spy_game([1,0,4,0,8,7]))
  def test_prime_conr(self):
      self.assertEqual(count_primes(50), 15)

if __name__ == '__main__':
    unittest.main()