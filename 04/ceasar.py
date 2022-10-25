#!/usr/bin/env python3
# encoding: utf-8

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ALPHABET_BIG = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
SHIFT = 2
TEXT = '''Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb'''


def isUpper(s):
    if s in ALPHABET_BIG:
        return True
    return False


def isLower(s):
    if s in ALPHABET:
        return True
    return False


def shiftedIndex(s, dict):
    return dict[(dict.index(s) + SHIFT) % 26]


def decypherToConsole(s):
    for char in s:
        if isUpper(char):
            print(shiftedIndex(char, ALPHABET_BIG), end='')
        elif isLower(char):
            print(shiftedIndex(char, ALPHABET), end='')
        else:
            print(char, end='')


def main():
    decypherToConsole(TEXT)


if __name__ == "__main__":
    main()
