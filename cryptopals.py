import base64
import collections
import itertools
import operator


def hex_to_base64(hexStr):
    return base64.b64encode(bytes.fromhex(hexStr))


def xor(a, b):
    return bytes(map(operator.xor, a, b))


def xorcrypt(key, cipher):
    return ''.join(chr(key ^ x) for x in cipher)


def alpha_count(text):
    return collections.Counter(text.upper())


def dist(count1, count2):
    keys = set(count1.keys()) | set(count2.keys())
    diffs = map(lambda x: abs(count1[x] - count2[x]), keys)
    return sum(diffs)


def expected_counts(total):
    freqs = collections.defaultdict(lambda: 0)
    freqs['A'] = 8.167
    freqs['B'] = 1.492
    freqs['C'] = 2.782
    freqs['D'] = 4.253
    freqs['E'] = 12.702
    freqs['F'] = 2.228
    freqs['G'] = 2.015
    freqs['H'] = 6.094
    freqs['I'] = 6.966
    freqs['J'] = 0.153
    freqs['K'] = 0.772
    freqs['L'] = 4.025
    freqs['M'] = 2.406
    freqs['N'] = 6.749
    freqs['O'] = 7.507
    freqs['P'] = 1.929
    freqs['Q'] = 0.095
    freqs['R'] = 5.987
    freqs['S'] = 6.327
    freqs['T'] = 9.056
    freqs['U'] = 2.758
    freqs['V'] = 0.978
    freqs['W'] = 2.360
    freqs['X'] = 0.150
    freqs['Y'] = 1.974
    freqs['Z'] = 0.074

    for c in freqs:
        freqs[c] = int(round(total * freqs[c] / 100.0))

    return freqs


def break_xor(cipher):
    plaintexts = map(lambda key: xorcrypt(key, cipher), range(256))
    return min(plaintexts, key=distance_from_english)


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
