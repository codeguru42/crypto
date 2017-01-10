from collections import Counter
from sys import argv

from cryptopals import grouper


def main():
    with open(argv[1]) as file:
        for line in file:
            data = bytes.fromhex(line.strip())
            print('data:', data)
            block_count = Counter(grouper(data, 16))
            print('blocks:', block_count)


if __name__ == "__main__":
    main()
