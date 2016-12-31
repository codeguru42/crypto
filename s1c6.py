import base64
import sys
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


def normalized_edit_distance(text, keylen):
    dist = hamming_distance(text[:keylen], text[keylen:2 * keylen])
    return dist / keylen


def best_keylen(filename):
    with open(filename) as file:
        first_line = base64.b64decode(file.readline())
        return min(range(2, 40), key=lambda l: normalized_edit_distance(first_line, l))


def main():
    print(best_keylen(sys.argv[1]))

if __name__ == "__main__":
    main()
