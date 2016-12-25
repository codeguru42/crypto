#!/usr/bin/python3
import sys
import cryptopals

def main():
  with open(sys.argv[1]) as file:
    plaintexts = map(lambda line : cryptopals.break_xor(bytes.fromhex(line.strip())), file)
    best = min(plaintexts, key=cryptopals.distance_from_english)
    print(best)

if __name__ == "__main__":
  main()
