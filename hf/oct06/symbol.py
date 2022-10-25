#!/usr/bin/env python3
# encoding: utf-8

def getTwoKTwentyTwoWithoutNumber() -> str:
    ''' Returns the year two thousand and twenty two without using a single number
    '''
    two = str(int(True) + int(True))
    zero = str(int(False))
    return ''.join([two, zero, two, two])


def main():
    print(getTwoKTwentyTwoWithoutNumber())


if __name__ == "__main__":
    main()
