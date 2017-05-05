from collections import Counter
from sys import argv

from cryptopals import grouper


def is_ecb(cipher):
    block_count = Counter(grouper(cipher, 16))
    ecb = False
    for block in block_count:
        if block_count[block] > 1:
            ecb = True
    return ecb


def main():
    with open(argv[1]) as file:
        for line_num, line in enumerate(file):
            data = bytes.fromhex(line.strip())
            if is_ecb(data):
                print("Line", line_num + 1)
                print(data)


if __name__ == "__main__":
    main()
