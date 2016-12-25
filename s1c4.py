#!/usr/bin/python3
import sys
import cryptopals

def main():
  with open(sys.argv[1]) as file:
    for line in file:
      b = bytes.fromhex(line.strip())
      print(cryptopals.break_xor(b))

if __name__ == "__main__":
  main()
