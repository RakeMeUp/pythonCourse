#!/usr/bin/env python3
# encoding: utf-8


def isPalindrome(s):
    return s == s[::-1]


def main():
    print(isPalindrome("helleh"))
    print(isPalindrome("helleg"))


if __name__ == "__main__":
    main()
