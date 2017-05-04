import unittest


class TestCbcEncrypt(unittest.TestCase):
    def testCase(self):
        key = b'YELLOW SUBMARINE'
        iv = b'\x00' * 16
        text = b'The quick red fox jumped over the lazy brown dog'
        cipher_text = cbc_encrypt(key, text, iv)
        self.assertEqual(text, cbc_decrypt(key, cipher_text, iv))


def cbc_encrypt(key, text, iv):
    pass


def cbc_decrypt(key, text, iv):
    pass


if __name__ == '__main__':
    unittest.main()
