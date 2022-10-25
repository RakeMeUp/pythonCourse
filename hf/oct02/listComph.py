#!/usr/bin/env python3
# encoding: utf-8

INPUT1 = ['auto', 'villamos', 'metro']
INPUT2 = ['aladar', 'bela', 'cecil']
INPUT3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
INPUT4 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
INPUT5 = "1234567"
INPUT6 = 'The quick brown fox jumps over the lazy dog'
INPUT8 = "python is an awesome language"
INPUT9 = [' apple ', ' banana ', ' kiwi']
INPUT10 = [1, 0, 1, 1, 0, 1, 0, 0]


def main():
    # 1.
    uppers = [s.upper() + '!' for s in INPUT1]
    print(uppers)
    # 2.
    capitaled = [s.capitalize() for s in INPUT2]
    print(capitaled)
    # 3.
    tenZero = [0 for s in range(10)]
    print(tenZero)
    # 4.
    double = [n*2 for n in range(1, 11)]
    print(double)
    # 5.
    toNum = [int(s) for s in INPUT4]
    print(toNum)
    # 6.
    toList = [int(char) for char in INPUT5]
    print(toList)
    # 7.
    wordsLength = [len(word) for word in INPUT6.split(' ')]
    print(wordsLength)
    # 8.
    initials = [word[0] for word in INPUT8.split(' ')]
    print(initials)
    # 9.
    listTuple = [(word, len(word)) for word in INPUT6.split(' ')]
    print(listTuple)
    # 10.
    evens = [n*2 for n in range(10)]
    print(evens)
    # 11.
    evensSquared = [n**2 for n in range(0, 20, 2)]
    print(evensSquared)
    # 12.
    squaredEndsWithFour = [n**2 for n in range(20) if str(n**2)[-1:] == "4"]
    print(squaredEndsWithFour)
    # 13.
    bigAlphabet = ''.join(
        [chr(char) for char in range(ord('A'), ord('Z') + 1)]
    )
    print(bigAlphabet)
    # 14.
    trimmed = [s.strip() for s in INPUT9]
    print(trimmed)
    # 15
    numToConcatStr = ''.join([str(n) for n in INPUT10])
    print(numToConcatStr)


if __name__ == "__main__":
    main()
