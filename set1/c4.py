#!/usr/bin/python3
import sys
import unittest

import cryptopals


class TestBreakAll(unittest.TestCase):
    def testCase(self):
        filename = 'input/set1/s1c4.txt'
        expected = (0x35, b'Now that the party is jumping\n')
        self.assertEqual(expected, break_file(filename))


def break_file(filename):
    with open(filename) as file:
        plaintexts = map(lambda line: cryptopals.break_xor(bytes.fromhex(line.strip())), file)
        return min(plaintexts, key=lambda text: cryptopals.distance_from_english(text[1]))


def main():
    print(break_file(sys.argv[1]))


if __name__ == "__main__":
    main()
