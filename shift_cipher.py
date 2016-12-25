import sys
import argparse


def shift(text, key):
  def shift_char(x):
    return chr((ord(x) - ord('A') + key) % 26 + ord('A'))
  return ''.join(map(shift_char, text.upper()))


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('key', type=int)
  parser.add_argument('filename', nargs='?', help='name of input file')
  args = parser.parse_args()

  if(args.filename):
    inf = open(args.filename)
  else:
    inf = sys.stdin

  for line in inf:
    print(shift(line.strip(), args.key))
  inf.close()

if __name__ == "__main__":
  main()
