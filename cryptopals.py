import base64

def hexToBase64(hexStr):
  return base64.b64encode(bytes.fromhex(hexStr))
