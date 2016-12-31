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


def best_keylen(data):
    return min(range(2, 40), key=lambda l: normalized_edit_distance(data, l))


def main():
    with open(sys.argv[1]) as file:
        data = base64.b64decode(file.read())
        print(best_keylen(data))

if __name__ == "__main__":
    main()
