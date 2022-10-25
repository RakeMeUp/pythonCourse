#!/usr/bin/env python3
# encoding: utf-8

def getSumOfMultiples(maxNum: int, firstMultiple: int, secondMultiple: int) -> int:
    '''Sums up multiples of "firstMultiple" or "secondMultiple" up to "max" -> [1 : ]max
    '''
    return sum([num for num in range(1, maxNum) if num % firstMultiple == 0 or num % secondMultiple == 0])


def main():

    print(getSumOfMultiples(1000, 3, 5))


if __name__ == "__main__":
    main()
