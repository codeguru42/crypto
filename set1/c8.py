from collections import Counter
from sys import argv

from cryptopals import grouper


def main():
    with open(argv[1]) as file:
        for line_num, line in enumerate(file):
            data = bytes.fromhex(line.strip())
            block_count = Counter(grouper(data, 16))
            is_aes = False
            for block in block_count:
                if block_count[block] > 1:
                    is_aes = True
            if is_aes:
                print("Line", line_num + 1)
                print(data)


if __name__ == "__main__":
    main()
