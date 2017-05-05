import base64
import collections
import itertools
import operator


def hex_to_base64(hexStr):
    return base64.b64encode(bytes.fromhex(hexStr))


def xor(a, b):
    return bytes(map(operator.xor, a, b))


def xorcrypt(key, cipher):
    return b''.join(xor(key, x) for x in grouper(cipher, len(key)))


def alpha_count(text):
    return collections.Counter(text)


def dist(count1, count2):
    keys = set(count1.keys()) | set(count2.keys())
    diffs = map(lambda x: abs(count1[x] - count2[x]), keys)
    return sum(diffs)


def expected_counts(total):
    freqs = collections.defaultdict(lambda: 0)
    freqs[ord('a')] = 8.167
    freqs[ord('b')] = 1.492
    freqs[ord('c')] = 2.782
    freqs[ord('d')] = 4.253
    freqs[ord('e')] = 12.702
    freqs[ord('f')] = 2.228
    freqs[ord('g')] = 2.015
    freqs[ord('h')] = 6.094
    freqs[ord('i')] = 6.966
    freqs[ord('j')] = 0.153
    freqs[ord('k')] = 0.772
    freqs[ord('l')] = 4.025
    freqs[ord('m')] = 2.406
    freqs[ord('n')] = 6.749
    freqs[ord('o')] = 7.507
    freqs[ord('p')] = 1.929
    freqs[ord('q')] = 0.095
    freqs[ord('r')] = 5.987
    freqs[ord('s')] = 6.327
    freqs[ord('t')] = 9.056
    freqs[ord('u')] = 2.758
    freqs[ord('v')] = 0.978
    freqs[ord('w')] = 2.360
    freqs[ord('x')] = 0.150
    freqs[ord('y')] = 1.974
    freqs[ord('z')] = 0.074

    for c in freqs:
        freqs[c] = int(round(total * freqs[c] / 100.0))

    return freqs


def break_xor(cipher):
    keys = range(256)
    plaintexts = map(lambda key: (key, xorcrypt((key,), cipher)), keys)
    return min(plaintexts, key=lambda text: distance_from_english(text[1]))


def distance_from_english(text):
    eng_count = expected_counts(len(text))
    count = alpha_count(text)
    return dist(count, eng_count)


def grouper(iterable, n):
    it = iter(iterable)
    group = tuple(itertools.islice(it, n))
    while group:
        yield group
        group = tuple(itertools.islice(it, n))


def pkcs7(text, block_length):
    if (len(text) % block_length == 0):
        return text
    padding = block_length - len(text)%block_length
    return text + bytes([padding] * padding)


def is_ecb(cipher):
    block_count = collections.Counter(grouper(cipher, 16))
    ecb = False
    for block in block_count:
        if block_count[block] > 1:
            ecb = True
    return ecb
