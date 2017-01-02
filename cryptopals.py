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
    return collections.Counter(text.upper())


def dist(count1, count2):
    keys = set(count1.keys()) | set(count2.keys())
    diffs = map(lambda x: abs(count1[x] - count2[x]), keys)
    return sum(diffs)


def expected_counts(total):
    freqs = collections.defaultdict(lambda: 0)
    freqs[ord('A')] = 8.167
    freqs[ord('B')] = 1.492
    freqs[ord('C')] = 2.782
    freqs[ord('D')] = 4.253
    freqs[ord('E')] = 12.702
    freqs[ord('F')] = 2.228
    freqs[ord('G')] = 2.015
    freqs[ord('H')] = 6.094
    freqs[ord('I')] = 6.966
    freqs[ord('J')] = 0.153
    freqs[ord('K')] = 0.772
    freqs[ord('L')] = 4.025
    freqs[ord('M')] = 2.406
    freqs[ord('N')] = 6.749
    freqs[ord('O')] = 7.507
    freqs[ord('P')] = 1.929
    freqs[ord('Q')] = 0.095
    freqs[ord('R')] = 5.987
    freqs[ord('S')] = 6.327
    freqs[ord('T')] = 9.056
    freqs[ord('U')] = 2.758
    freqs[ord('V')] = 0.978
    freqs[ord('W')] = 2.360
    freqs[ord('X')] = 0.150
    freqs[ord('Y')] = 1.974
    freqs[ord('Z')] = 0.074

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
