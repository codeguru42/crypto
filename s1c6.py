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


class TestTranspose(unittest.TestCase):
    def testCase(self):
        l = [list(range(5 * i, 5 * i + 5)) for i in range(5)]
        expected = [list(range(i, 25, 5)) for i in range(5)]
        self.assertEqual(expected, transpose(l))


def hamming_distance(str1, str2):
    temp = cryptopals.xor(str1, str2)
    return sum(bitstring.Bits(temp))


def normalized_edit_distance(text, keylen):
    dist = hamming_distance(text[:keylen], text[keylen:2 * keylen])
    return dist / keylen


def best_keylen(data):
    return min(range(2, 40), key=lambda l: normalized_edit_distance(data, l))


def transpose(lines):
    result = [[] for _ in lines[0]]
    for row in lines:
        for x, new_row in zip(row, result):
            new_row.append(x)
    return result


def main():
    with open(sys.argv[1]) as file:
        data = base64.b64decode(file.read())
        print('data:', data)
        print(len(data), 'bytes')
        keylen = best_keylen(data)
        print('keylen:', keylen)
        groups = transpose(list(cryptopals.grouper(data, keylen)))
        print('groups:', groups)
        key = [cryptopals.break_xor(g) for g in groups]
        print('key: ', key)
        print(len(key), 'bytes')
        plain = [''.join(chr(x) for x in row) for row in transpose(key)]
        print(''.join(plain))


if __name__ == "__main__":
    main()
