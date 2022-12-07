#!/usr/bin/env python3
# encoding: utf-8

import random


def shuffled(li):
    temp = li[:]
    random.shuffle(temp)
    return temp


def main():
    li = [1, 2, 3]
    temp = shuffled(li)
    print(temp)
    print(li)


if __name__ == "__main__":
    main()
