import secrets

from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad


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
        aes = AES.new(key, mode)
    else:
        aes = AES.new(key, mode, iv=iv)

    prefix = random_bytes(rng.randrange(5, 11))
    suffix = random_bytes(rng.randrange(5, 11))
    plain = pad(prefix + plain + suffix, block_size)
    return aes.encrypt(plain)


def main():
    for i in range(10):
        text = b'The quick red fox jumped over the lazy brown dog.'
        print(encrypt_with_random_key(text))


if __name__ == '__main__':
    main()
