#!/usr/bin/env python3
# encoding: utf-8

def invCapcha(capcha):
    """Returns the sum of those digits, what equals with their next digit."""
    occurList = [int(capcha[i - 1])
                 for i in range(len(capcha)) if capcha[i - 1] == capcha[i]]
    return sum(occurList)


def main():
    capchas = ["1122", "1111", "1234", "91212129"]
    for capcha in capchas:
        print(capcha + ":\t" + str(invCapcha(capcha)))


if __name__ == "__main__":
    main()
