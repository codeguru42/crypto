import base64
import binascii
import string
import collections

def hexToBase64(hexStr):
  return base64.b64encode(bytes.fromhex(hexStr))

def xor(a, b):
  xs = bytes.fromhex(a)
  ys = bytes.fromhex(b)
  c = bytearray()
  for x, y in zip(xs, ys):
    c.append(x ^ y)
  return binascii.hexlify(c)

def xorcrypt(key, cipher):
  return ''.join([chr(key ^ x) for x in cipher])

def asciiUpper(text):
  for c in text:
    i = string.ascii_lowercase.find(c)
    if i == -1:
      yield c
    else:
      yield c.upper()

def alphaCount(text):
  return collections.Counter(text.upper())

def dist(count1, count2):
  keys = set(count1.keys()) | set(count2.keys())
  diffs = map(lambda x: abs(count1[x] - count2[x]), keys)
  return sum(diffs)

def expectedCounts(total):
  freqs = collections.defaultdict(lambda : 0)
  freqs['A'] = total *  8.167 / 100.0
  freqs['B'] = total *  1.492 / 100.0
  freqs['C'] = total *  2.782 / 100.0
  freqs['D'] = total *  4.253 / 100.0
  freqs['E'] = total * 12.702 / 100.0
  freqs['F'] = total *  2.228 / 100.0
  freqs['G'] = total *  2.015 / 100.0
  freqs['H'] = total *  6.094 / 100.0
  freqs['I'] = total *  6.966 / 100.0
  freqs['J'] = total *  0.153 / 100.0
  freqs['K'] = total *  0.772 / 100.0
  freqs['L'] = total *  4.025 / 100.0
  freqs['M'] = total *  2.406 / 100.0
  freqs['N'] = total *  6.749 / 100.0
  freqs['O'] = total *  7.507 / 100.0
  freqs['P'] = total *  1.929 / 100.0
  freqs['Q'] = total *  0.095 / 100.0
  freqs['R'] = total *  5.987 / 100.0
  freqs['S'] = total *  6.327 / 100.0
  freqs['T'] = total *  9.056 / 100.0
  freqs['U'] = total *  2.758 / 100.0
  freqs['V'] = total *  0.978 / 100.0
  freqs['W'] = total *  2.360 / 100.0
  freqs['X'] = total *  0.150 / 100.0
  freqs['Y'] = total *  1.974 / 100.0
  freqs['Z'] = total *  0.074 / 100.0
  return freqs
