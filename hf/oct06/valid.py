#!/usr/bin/env python3
# encoding: utf-8


def valid(text: str, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") -> str:
    """Returns a string, made out of characters that are found in the 'chars' parameter"""
    result = []
    splitted = list(text)
    for char in splitted:
        if char in chars:
            result.append(char)
    return "".join(result)


def main():
    print(valid("Barking!"))
    print(valid("KL754", "0123456789"))
    print(valid("BEAN", "abcdefghijklmnopqrstuvwxyz"))


if __name__ == "__main__":
    main()
