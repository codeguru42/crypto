import unittest
from Cryptodome.Cipher import AES
from cryptopals import grouper, xor


class TestCbcEncrypt(unittest.TestCase):
    def testCase(self):
        key = b'YELLOW SUBMARINE'
        iv = b'\x00' * 16
        text = b'The quick red fox jumped over the lazy brown dog'
        cipher_text = cbc_encrypt(key, text, iv)
        print(cipher_text)
        self.assertEqual(text, cbc_decrypt(key, cipher_text, iv))


def cbc_encrypt(key, text, iv):
    aes = AES.new(key, AES.MODE_ECB)
    cipher_text = []
    data = iv
    for block in grouper(text, 16):
        data = xor(data, bytes(block))
        cipher_text.append(aes.encrypt(data))
    return b''.join(cipher_text)


def cbc_decrypt(key, text, iv):
    pass


def main():
    pass


if __name__ == '__main__':
    main()
