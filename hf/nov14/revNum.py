#!/usr/bin/env python3
# encoding: utf-8


def reverseNumber(num):
    return int(str(num)[::-1])


def main():
    print(reverseNumber(1235))


if __name__ == "__main__":
    main()
