import sys
import argparse

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('filename', nargs='?', help='name of input file')
  args = parser.parse_args()
  if(args.filename):
    inf = open(args.filename)
  else:
    inf = sys.stdin

  for line in inf:
    print(line.strip())
  inf.close()

if __name__ == "__main__":
  main()
