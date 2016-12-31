#!/usr/bin/python3
import sys
import unittest

import cryptopals


class TestBreakAll(unittest.TestCase):
    def testCase(self):
        filename = 's1c4.txt'
        expected = b'nOW\x00THAT\x00THE\x00PARTY\x00IS\x00JUMPING*'
        self.assertEqual(expected, break_file(filename))


def break_file(filename):
    with open(filename) as file:
        plaintexts = map(lambda line: cryptopals.break_xor(bytes.fromhex(line.strip()), 1), file)
        return min(plaintexts, key=cryptopals.distance_from_english)


def main():
    print(break_file(sys.argv[1]))


if __name__ == "__main__":
    main()
