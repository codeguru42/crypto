from base64 import b64decode
from sys import argv

from Crypto.Cipher import AES


def main():
    key = "YELLOW SUBMARINE"
    with open(argv[1]) as file:
        data = b64decode(file.read())
        print('data:', data)
        aes = AES.new(key)
        plaintext = aes.decrypt(data)
        print(plaintext.decode('ascii'))


if __name__ == "__main__":
    main()
