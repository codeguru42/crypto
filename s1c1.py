#!/usr/bin/python
import boltons.iterutils as iterutils

def main():
  hexString = raw_input()
  bytesList = []

  for hexByte in iterutils.chunked(hexString, 2):
    bytesList.append(int(hexByte, 16))

  print(bytesList)

if (__name__ == "__main__"):
  main()
