import unittest


class TestPkcs7(unittest.TestCase):
    def testCase(self):
        text = b'YELLOW SUBMARINE'
        expected = b'YELLOW SUBMARINE\x04\x04\x04\x04'
        actual = pkcs7(text, 20)
        self.assertEqual(expected, actual)


def pkcs7(text, block_length):
    padding = block_length - len(text)
    return text + bytes([padding] * padding)


if __name__ == '__main__':
    unittest.main()