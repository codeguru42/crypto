#!/usr/bin/python3
def main():
  file = open("s1c4.txt")
  for line in file:
    b = bytes.fromhex(line.strip())
    print(b)

if __name__ == "__main__":
  main()
