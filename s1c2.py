#!/usr/bin/python3
import cryptopals
import unittest

class TestXor(unittest.TestCase):
  def testCase(self):
    a = "1c0111001f010100061a024b53535009181c"
    b = "686974207468652062756c6c277320657965"
    expected = "746865206b696420646f6e277420706c6179"
    actual = cryptopals.xor(a, b)
    self.assertEqual(expected, actual)

if __name__ == "__main__":
  unittest.main()
