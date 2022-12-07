#!/usr/bin/env python3
# encoding: utf-8

import json
from pprint import pprint


def main():
    with open("json_data.json", "r") as infile:
        d = json.load(infile)
        print(type(d))
        count = 0
        for (key, value) in d.items():
            if key == key[::-1]:
                print(value)
                count += 1
        print("amount of palindromes: " + str(count))


if __name__ == "__main__":
    main()
