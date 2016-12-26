import argparse
import sys
import unittest

import cryptopals


class TestViginere(unittest.TestCase):
    def testCase(self):
        key = 'zzzyyyxxx'
        data = 'UibpmuOdbofNgttbFksjtvocvwrzpvvqq'
        expected = 'THANKSLAYNEMERRYCHRISTMASTOYOUTOO'
        self.assertEqual(expected, viginere(key, data))


def viginere(key, text):
    def char_to_int(c):
        return ord(c) - ord('A')

    def str_to_ints(s):
        return list(char_to_int(x) for x in s.upper())

    key_int = str_to_ints(key)
    text_int = str_to_ints(text)
    cipher = [map(lambda x, y: (x + y) % 26, key_int, text_group) for text_group in
              cryptopals.grouper(text_int, len(key_int))]
    cipher = ((chr(c + ord('A')) for c in x) for x in cipher)
    return ''.join(''.join(x) for x in cipher)


def break_viginere(cipher):
    pass


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-k', '--key', help='encryption key')
    group.add_argument('-b', '--break-cipher', help='break encryption', action='store_true')
    parser.add_argument('filename', nargs='?', help='name of input file')
    args = parser.parse_args()

    if args.filename:
        inf = open(args.filename)
    else:
        inf = sys.stdin

    for line in inf:
        if args.break_cipher:
            break_viginere(line.strip())
        else:
            print('viginere:', viginere(args.key, line.strip()))
    inf.close()


if __name__ == "__main__":
    main()
