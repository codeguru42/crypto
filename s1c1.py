#!/usr/bin/python
import boltons.iterutils as iterutils

hexString = raw_input()

for hexByte in iterutils.chunked(hexString, 2):
  print hexByte
