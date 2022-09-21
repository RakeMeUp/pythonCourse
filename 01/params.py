#!/usr/bin/env python3
# encoding: utf-8

import sys


def main():
    str = sys.argv[1]
    if str == "Batman" or str == "Robin":
        print("Szevasz " + str + "!")
    else:
        print("Denever veszely")


if __name__ == "__main__":
    main()
