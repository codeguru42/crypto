import base64
import binascii

def hexToBase64(hexStr):
  return base64.b64encode(bytes.fromhex(hexStr))

def xor(a, b):
  xs = bytes.fromhex(a)
  ys = bytes.fromhex(b)
  c = bytearray()
  for x, y in zip(xs, ys):
    c.append(x ^ y)
  return binascii.hexlify(c)
