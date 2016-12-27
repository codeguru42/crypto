#!/usr/bin/python3
import sys
import unittest

import cryptopals


class TestBreakAll(unittest.TestCase):
    def testCase(self):
        filename = 's1c4.txt'
        expected = b'nOW\x00THAT\x00THE\x00PARTY\x00IS\x00JUMPING*'
        with open(filename) as file:
            plaintexts = map(lambda line: cryptopals.break_xor(bytes.fromhex(line.strip())), file)
            best = min(plaintexts, key=cryptopals.distance_from_english)
            self.assertEqual(expected, best)


def main():
    with open(sys.argv[1]) as file:
        plaintexts = map(lambda line: cryptopals.break_xor(bytes.fromhex(line.strip())), file)
        best = min(plaintexts, key=cryptopals.distance_from_english)
        print(repr(best))


if __name__ == "__main__":
    main()
