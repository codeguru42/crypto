import secrets


def random_key(keylen):
    rng = secrets.SystemRandom()
    return bytes(rng.sample(range(256), keylen))


def main():
    for i in range(10):
        print(random_key(16))


if __name__ == '__main__':
    main()
