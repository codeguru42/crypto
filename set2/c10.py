import unittest
from Cryptodome.Cipher import AES
from cryptopals import grouper, xor


class TestCbc(unittest.TestCase):
    def setUp(self):
        self.key = b'YELLOW SUBMARINE'
        self.iv = b'\x00' * 16
        self.text = b'The quick red fox jumped over the lazy brown dog'
        self.aes = AES.new(self.key, AES.MODE_CBC, iv=self.iv)

    def testEncrypt(self):
        expected = self.aes.encrypt(self.text)
        actual = cbc_encrypt(self.key, self.text, self.iv)
        self.assertEqual(expected, actual)


def cbc_encrypt(key, plain, iv):
    aes = AES.new(key, AES.MODE_ECB)
    cipher_text = []
    data = iv
    for block in grouper(plain, 16):
        data = xor(data, bytes(block))
        data = aes.encrypt(data)
        cipher_text.append(data)
    return b''.join(cipher_text)


def cbc_decrypt(key, text, iv):
    pass


def main():
    pass


if __name__ == '__main__':
    main()
