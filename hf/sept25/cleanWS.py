#!/usr/bin/env python3
# encoding: utf-8

def cleanWhitespace(string):
    return ''.join(string.split())


def main():
    print(cleanWhitespace("206.130.99.82: \n8080"))
    print(cleanWhitespace("192.20.246.138:\n 6666"))


if __name__ == "__main__":
    main()
