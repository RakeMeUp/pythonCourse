#!/usr/bin/env python3
# encoding: utf-8
from ast import Num
import sys


def main():
    if (len(sys.argv) == 3):
        print(int(sys.argv[1]) + int(sys.argv[2]))
    else:
        print("error")


if __name__ == "__main__":
    main()
