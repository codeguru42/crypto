import secrets


def random_key(keylen):
    rng = secrets.SystemRandom()
    return rng.sample(xrange(256), keylen)
