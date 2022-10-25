#!/usr/bin/env python3
# encoding: utf-8

from pickletools import string1


STR1 = "python"
STR2 = None


def xor(pred1, pred2):
    if (pred1 and not pred2) or (pred2 and not pred1):
        return True
    return False


def main():
    print(xor(STR1, STR2))
    print(xor(False, False))
    print(xor(False, True))
    print(xor(True, False))
    print(xor(True, True))


if __name__ == "__main__":
    main()
