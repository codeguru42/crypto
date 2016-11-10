#!/usr/bin/python3
def main():
  msg = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
  cipher = bytes.fromhex(msg)
  print("cipher: ", cipher)

  for key in range(256):
    plain = ''.join([chr(key ^ x) for x in cipher])
    if plain.isalpha():
      print(plain)

if __name__ == "__main__":
  main()
