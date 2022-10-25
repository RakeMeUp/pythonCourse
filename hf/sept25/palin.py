#!/usr/bin/env python3
# encoding: utf-8

from operator import truediv
from pickle import FALSE


def isPalindrome(s):
    if s == s[::-1]:
        return True
    return False


def isPalindromeRecursion(s):
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    return isPalindromeRecursion(s[1:-1])


def isPalindromeIterative(s):
    result = True
    revS = s[::-1]
    i = 0
    while i < len(s):
        if s[i] != revS[i]:
            result = False
        i += 1
    return result


def main():
    print(isPalindrome('abba'))
    print(isPalindromeRecursion('abba'))
    print(isPalindromeIterative('abba'))
    print(isPalindrome('abbax'))
    print(isPalindromeRecursion('abbax'))
    print(isPalindromeIterative('abbax'))


if __name__ == "__main__":
    main()
