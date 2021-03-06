#!/usr/bin/python3
import unittest

import cryptopals


class TestXor(unittest.TestCase):
    def testCase(self):
        a = "1c0111001f010100061a024b53535009181c"
        b = "686974207468652062756c6c277320657965"
        expected = bytes.fromhex("746865206b696420646f6e277420706c6179")
        actual = cryptopals.xor(bytes.fromhex(a), bytes.fromhex(b))
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
