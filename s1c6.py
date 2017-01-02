import base64
import sys
import unittest

import bitstring
import itertools

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
    total = 0
    count = 4
    for a, b in itertools.islice(window(cryptopals.grouper(text, keylen), 2), count):
        dist = hamming_distance(a, b)
        total += dist / keylen
    return total / count


def keylen_gen(data, min_len, max_len):
    return sorted(range(min_len, max_len), key=lambda l: normalized_edit_distance(data, l))


def transpose(lines):
    result = [[] for _ in lines[0]]
    for row in lines:
        for x, new_row in zip(row, result):
            new_row.append(x)
    return result


def window(seq, n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(itertools.islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def break_repeating_xor(data, keylen):
    groups = transpose(list(cryptopals.grouper(data, keylen)))
    plaintext_groups = [cryptopals.break_xor(g) for g in groups]
    plaintext = [bytes(row) for row in transpose(plaintext_groups)]
    return b''.join(plaintext)


def main():
    with open(sys.argv[1]) as file:
        data = base64.b64decode(file.read())
        print('data:', data)
        print(len(data), 'bytes')
        keylens = keylen_gen(data, 2, 40)
        plain = min((break_repeating_xor(data, l) for l in keylens[:5]), key=cryptopals.distance_from_english)
        print(plain)


if __name__ == "__main__":
    main()
