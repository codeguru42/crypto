import unittest
import bitstring

import cryptopals


class TestHammingDistance(unittest.TestCase):
    def testCase(self):
        str1 = b'this is a test'
        str2 = b'wokka wokka!!!'
        expected = 37
        self.assertEqual(expected, hamming_distance(str1, str2))


def hamming_distance(str1, str2):
    temp = cryptopals.xor(str1, str2)
    return sum(bitstring.Bits(temp))


if __name__ == "__main__":
    unittest.main()
