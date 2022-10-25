#!/usr/bin/env python3
# encoding: utf-8

def innerMultiply(li):
    result = 1
    for e in li:
        result *= e

    return result


def main():
    a = [1, 2, 5, 6, 4, 2, 1, 2]

    print(innerMultiply(a))


if __name__ == "__main__":
    main()
