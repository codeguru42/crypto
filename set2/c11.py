import secrets
from unittest import TestCase
from unittest.mock import patch

from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad

from cryptopals import is_ecb


class TestOracle(TestCase):
    def testDetectECB(self):
        print('Testing ECB')
        with patch.object(secrets.SystemRandom, 'randrange', side_effect=[AES.MODE_ECB, 5, 5]) as mock_rng:
            text = b'The quick red fox jumped over the lazy brown dog.'
            cipher = encrypt_with_random_key(text)
            self.assertTrue(is_ecb(cipher))

    def testDetectCBC(self):
        pass


def random_bytes(byte_count):
    rng = secrets.SystemRandom()
    return bytes(rng.choices(range(256), k=byte_count))


def encrypt_with_random_key(plain):
    key_length = 16
    block_size = 16
    rng = secrets.SystemRandom()
    key = random_bytes(key_length)
    mode = rng.randrange(1, 3)
    iv = random_bytes(block_size)

    if mode == AES.MODE_ECB:
        print('ECB mode')
        aes = AES.new(key, mode)
    else:
        print('CBC mode')
        aes = AES.new(key, mode, iv=iv)

    prefix = random_bytes(rng.randrange(5, 11))
    suffix = random_bytes(rng.randrange(5, 11))
    plain = pad(prefix + plain + suffix, block_size)
    return aes.encrypt(plain)


def main():
    for i in range(10):
        text = b'The quick red fox jumped over the lazy brown dog.'
        cipher = encrypt_with_random_key(text)
        if is_ecb(cipher):
            print('ECB')
        else:
            print('CBC')


if __name__ == '__main__':
    main()
