import unittest
from checksum import *

class TestMymethodsMethods(unittest.TestCase):

  def test_validchksum(self):
      self.assertEqual(checksum(4386280022458750),'Valid')
  def test_invalidchksum(self):
      self.assertEqual(checksum(43862800224587),'Not Valid')

if __name__ == '__main__':
    unittest.main()
