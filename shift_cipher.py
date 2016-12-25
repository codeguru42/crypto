import argparse
import sys


def shift(key, text):
    def shift_char(x):
        return chr((ord(x) - ord('A') + key) % 26 + ord('A'))

    return ''.join(map(shift_char, text.upper()))


def break_shift(cipher):
    plaintexts = (shift(key, cipher.upper()) for key in range(26))
    for plain in plaintexts:
        print(plain)


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-k', '--key', type=int, help='encryption key')
    group.add_argument('-b', '--break-cipher', help='break encryption', action='store_true')
    parser.add_argument('filename', nargs='?', help='name of input file')
    args = parser.parse_args()

    if (args.filename):
        inf = open(args.filename)
    else:
        inf = sys.stdin

    for line in inf:
        if (args.break_cipher):
            break_shift(line.strip())
        else:
            print(shift(args.key, line.strip()))
    inf.close()


if __name__ == "__main__":
    main()
