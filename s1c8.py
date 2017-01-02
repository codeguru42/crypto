from base64 import b64decode
from sys import argv

from Crypto.Cipher import AES


def main():
    with open(argv[1]) as file:
        for line in file:
            data = bytes.fromhex(line)
            print('data:', data)


if __name__ == "__main__":
    main()
