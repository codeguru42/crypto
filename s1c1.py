#!/usr/bin/python3
import base64
import unittest

class TestHexToBase64(unittest.TestCase):
  def testCase(self):
    hexStr = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    expected = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    actual = base64.b64encode(bytes.fromhex(hexStr))
    self.assertEqual(expected, actual)

if (__name__ == "__main__"):
  unittest.main()
