from secrets import SystemRandom
from unittest import TestCase
from unittest.mock import patch
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad

from cryptopals import is_ecb


class TestOracle(TestCase):
    def testDetectECB(self):
        with patch.object(SystemRandom, 'randrange', side_effect=[AES.MODE_ECB, 5, 5]) as _:
            self.assertTrue(detect_ecb(encryption_oracle))

    def testDetectCBC(self):
        with patch.object(SystemRandom, 'randrange', side_effect=[AES.MODE_CBC, 5, 5]) as _:
            self.assertFalse(detect_ecb(encryption_oracle))


def random_bytes(byte_count):
    rng = SystemRandom()
    return bytes(rng.choices(range(256), k=byte_count))


def encryption_oracle(plain):
    key_length = 16
    block_size = 16
    rng = SystemRandom()
    key = random_bytes(key_length)
    mode = rng.randrange(1, 3)
    iv = random_bytes(block_size)

    if mode == AES.MODE_ECB:
        aes = AES.new(key, mode)
    else:
        aes = AES.new(key, mode, iv=iv)

    prefix = random_bytes(rng.randrange(5, 11))
    suffix = random_bytes(rng.randrange(5, 11))
    plain = pad(prefix + plain + suffix, block_size)
    return aes.encrypt(plain)


def detect_ecb(encryption_function):
    text = b'A' * 50
    cipher = encryption_function(text)
    return is_ecb(cipher)


def main():
    for i in range(10):
        text = b'The quick red fox jumped over the lazy brown dog.'
        cipher = encryption_oracle(text)
        if is_ecb(cipher):
            print('ECB')
        else:
            print('CBC')


if __name__ == '__main__':
    main()
