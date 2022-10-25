#!/usr/bin/env python3
# encoding: utf-8

def diamondToConsole(height):
    for n in range(height):
        print(" "*(height-n), "*"*(n*2+1))
    for n in range(height-2, -1, -1):
        print(" "*(height-n), "*"*(n*2+1))


def main():
    diamondToConsole(3)
    diamondToConsole(5)


if __name__ == "__main__":
    main()
