#!/usr/bin/python3

def main():
  hexString = input()
  bytesList = bytes.fromhex(hexString)
  print(bytesList)

if (__name__ == "__main__"):
  main()
