#!/usr/bin/env python3
# encoding: utf-8
from math import sqrt
import json


def main():
    # Source: https://hu.wikipedia.org/wiki/Eratoszthen%c3%a9sz_szit%c3%a1ja
    n = 10000000
    dict = {}
    lst = [True] * n
    for i in range(2, int(sqrt(n)) + 1):
        if lst[i]:
            for j in range(i * i, n, i):
                lst[j] = False
    for i in range(2, n):
        if lst[i]:
            dict.update({i: i})

    with open("json_data.json", "w") as outfile:
        json.dump(dict, outfile)


if __name__ == "__main__":
    main()
