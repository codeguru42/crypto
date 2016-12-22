#!/usr/bin/python3
import sys
import cryptopals

def main():
  msg = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
  cipher = bytes.fromhex(msg)
  print("cipher: ", cipher)

  engCount = cryptopals.expectedCounts(len(cipher))
  minDist = sys.maxsize
  bestPlain = ''
  for key in range(256):
    plain = cryptopals.xorcrypt(key, cipher)
    currCount = cryptopals.alphaCount(plain)
    currDist = cryptopals.dist(currCount, engCount)
    if currDist < minDist:
      minDist = currDist
      bestCount = currCount
      bestPlain = plain

  print("engCount:", engCount)
  print("bestPlain:", bestPlain)
  print("minDist:", minDist)
  print("bestCount:", bestCount)
  print("key:", key)

if __name__ == "__main__":
  main()
