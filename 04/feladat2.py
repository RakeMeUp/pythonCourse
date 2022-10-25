#!/usr/bin/env python3
# encoding: utf-8

INPUT1 = ['auto', 'villamos', 'metro']
INPUT2 = ['aladar', 'bela', 'cecil']
INPUT3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
INPUT4 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
INPUT5 = "1234567"
INPUT6 = 'The quick brown fox jumps over the lazy dog'


def main():
    uppers = [s.upper() + '!' for s in INPUT1]
    print(uppers)
    capitaled = [s.capitalize() for s in INPUT2]
    print(capitaled)
    tenZero = [0 for s in range(10)]
    print(tenZero)
    double = [n*2 for n in range(1, 11)]
    print(double)
    toNum = [int(s) for s in INPUT4]
    print(toNum)
    toList = [int(char) for char in INPUT5]
    print(toList)
    wordsLength = [len(words) for words in INPUT6.split(' ')]
    print(wordsLength)


if __name__ == "__main__":
    main()
