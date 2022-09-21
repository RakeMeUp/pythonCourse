#!/usr/bin/env python3
# encoding: utf-8

def isPalindrome(s):
    print(s == s[::-1])


def main():
    isPalindrome("helleh")
    isPalindrome("helleg")


if __name__ == "__main__":
    main()
