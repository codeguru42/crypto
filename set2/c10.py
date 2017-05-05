import unittest
from base64 import b64decode
from sys import argv

from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad

from cryptopals import grouper, xor, pkcs7


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

    def testEncryptPadding(self):
        text = pad(self.text[:25], 16)
        expected = self.aes.encrypt(text)
        actual = cbc_encrypt(self.key, self.text[:25], self.iv)
        self.assertEqual(expected, actual)

    def testDecrypt(self):
        cipher = self.aes.encrypt(self.text)
        aes_decrypt = AES.new(self.key, AES.MODE_CBC, iv = self.iv)
        expected = aes_decrypt.decrypt(cipher)
        my_cipher = cbc_encrypt(self.key, self.text, self.iv)
        actual = cbc_decrypt(self.key, my_cipher, self.iv)
        self.assertEqual(expected, actual)

    def testDecryptPadding(self):
        text = pad(self.text[:25], 16)
        cipher = self.aes.encrypt(text)
        aes_decrypt = AES.new(self.key, AES.MODE_CBC, iv = self.iv)
        expected = aes_decrypt.decrypt(cipher)
        my_cipher = cbc_encrypt(self.key, text, self.iv)
        actual = cbc_decrypt(self.key, my_cipher, self.iv)
        self.assertEqual(expected, actual)


def cbc_encrypt(key, plain, iv):
    block_size = 16
    aes = AES.new(key, AES.MODE_ECB)
    cipher_text = []
    data = iv
    plain = pkcs7(plain, block_size)
    for block in grouper(plain, block_size):
        data = xor(data, bytes(block))
        data = aes.encrypt(data)
        cipher_text.append(data)
    return b''.join(cipher_text)


def cbc_decrypt(key, cipher, iv):
    block_size = 16
    aes = AES.new(key, AES.MODE_ECB)
    cipher_text = []
    data = iv
    cipher = pkcs7(cipher, block_size)
    for block in grouper(cipher, block_size):
        plain = aes.decrypt(bytes(block))
        cipher_text.append(xor(plain, data))
        data = bytes(block)
    return b''.join(cipher_text)


def main():
    key = b'YELLOW SUBMARINE'
    iv = b'\x00' * 16
    with open(argv[1]) as file:
        cipher = b64decode(file.read())
        plain = cbc_decrypt(key, cipher, iv)
        print(plain.decode('ascii'))


if __name__ == '__main__':
    main()
