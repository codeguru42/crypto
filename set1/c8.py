from sys import argv

from cryptopals import is_ecb


def main():
    with open(argv[1]) as file:
        for line_num, line in enumerate(file):
            data = bytes.fromhex(line.strip())
            if is_ecb(data):
                print("Line", line_num + 1)
                print(data)


if __name__ == "__main__":
    main()
