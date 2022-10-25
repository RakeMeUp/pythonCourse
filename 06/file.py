#!/usr/bin/env python3
# encoding: utf-8

def main():
    f = open("text.txt", "r")

    for line in f:
        if line.endswith("sor\n"):
            print(line, end="")

    tartalom = f.read()
    print("'" + tartalom + "'")
    f.close()


if __name__ == "__main__":
    main()
