#!/usr/bin/python3
import unittest

import cryptopals


class TestOneByteXor(unittest.TestCase):
    def testCase(self):
        msg = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
        cipher = bytes.fromhex(msg)
        expected = b"Cooking MC's like a pound of bacon"
        self.assertEqual(expected, cryptopals.break_xor(cipher, 1))


if __name__ == "__main__":
    unittest.main()
