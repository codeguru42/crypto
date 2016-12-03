#!/usr/bin/python3
def xorcrypt(key, cipher):
  return ''.join([chr(key ^ x) for x in cipher])

def alphaCount(text):
  counts = [0] * 256
  for c in asciiUpper(text):
    counts[ord(c)] += 1
  return counts

def dist(count1, count2):
  diffs = map(lambda x, y: abs(x - y), count1, count2)
  return sum(diffs)

def expectedCounts(total):
  freqs = [0] * 256
  freqs[ord('a')] = total *  8.167 / 100.0
  freqs[ord('b')] = total *  1.492 / 100.0
  freqs[ord('c')] = total *  2.782 / 100.0
  freqs[ord('d')] = total *  4.253 / 100.0
  freqs[ord('e')] = total * 12.702 / 100.0
  freqs[ord('f')] = total *  2.228 / 100.0
  freqs[ord('g')] = total *  2.015 / 100.0
  freqs[ord('h')] = total *  6.094 / 100.0
  freqs[ord('i')] = total *  6.966 / 100.0
  freqs[ord('j')] = total *  0.153 / 100.0
  freqs[ord('k')] = total *  0.772 / 100.0
  freqs[ord('l')] = total *  4.025 / 100.0
  freqs[ord('m')] = total *  2.406 / 100.0
  freqs[ord('n')] = total *  6.749 / 100.0
  freqs[ord('o')] = total *  7.507 / 100.0
  freqs[ord('p')] = total *  1.929 / 100.0
  freqs[ord('q')] = total *  0.095 / 100.0
  freqs[ord('r')] = total *  5.987 / 100.0
  freqs[ord('s')] = total *  6.327 / 100.0
  freqs[ord('t')] = total *  9.056 / 100.0
  freqs[ord('u')] = total *  2.758 / 100.0
  freqs[ord('v')] = total *  0.978 / 100.0
  freqs[ord('w')] = total *  2.360 / 100.0
  freqs[ord('x')] = total *  0.150 / 100.0
  freqs[ord('y')] = total *  1.974 / 100.0
  freqs[ord('z')] = total *  0.074 / 100.0
  return freqs

def main():
  msg = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
  cipher = bytes.fromhex(msg)
  print("cipher: ", cipher)

  for key in range(256):
    plain = xorcrypt(key, cipher)
    if plain.isalpha():
      print(plain)

if __name__ == "__main__":
  main()
