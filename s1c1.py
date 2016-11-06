#!/usr/bin/python
import boltons.iterutils as iterutils

hex = raw_input()

for byte in iterutils.chunked(hex, 2):
  print byte
