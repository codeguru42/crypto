import unittest


class TestPkcs7(unittest.TestCase):
    def testCase(self):
        text = b'YELLOW SUBMARINE'
        expected = b'YELLOW SUBMARINE\x04\x04\x04\x04'
        actual = pkcs7(text)
        self.assertEqual(expected, actual)


def pkcs7(text):
    pass


if __name__ == '__main__':
    unittest.main()
