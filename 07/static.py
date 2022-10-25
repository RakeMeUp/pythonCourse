#!/usr/bin/env python3
# encoding: utf-8

class Counter:
    count = 0

    def __init__(self) -> None:
        Counter.count += 1

    def printCount():
        print(Counter.count)


def main():
    obj1 = Counter()
    obj2 = Counter()
    obj3 = Counter()
    Counter.printCount()


if __name__ == "__main__":
    main()
