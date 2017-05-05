import unittest

from cryptopals import pkcs7


class TestPkcs7(unittest.TestCase):
    def testBlockSize20(self):
        text = b'YELLOW SUBMARINE'
        expected = b'YELLOW SUBMARINE\x04\x04\x04\x04'
        actual = pkcs7(text, 20)
        self.assertEqual(expected, actual)

    def testBlockSize6(self):
        text = b'YELLOW SUBMARINE'
        expected = b'YELLOW SUBMARINE\x02\x02'
        actual = pkcs7(text, 6)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
