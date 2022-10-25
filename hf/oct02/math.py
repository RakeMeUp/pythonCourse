#!/usr/bin/env python3
# encoding: utf-8

def negyzetosszeg(num):
    return sum([n**2 for n in range(1, num+1)])


def osszegnegyzet(num):
    return sum(range(1, num+1))**2


def main():
    print(osszegnegyzet(10) - negyzetosszeg(10))
    print(osszegnegyzet(10))
    print(negyzetosszeg(10))


if __name__ == "__main__":
    main()
