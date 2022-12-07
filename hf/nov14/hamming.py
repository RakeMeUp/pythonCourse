#!/usr/bin/env python3
# encoding: utf-8


def hamming_distance(str1, str2):
    lengthOfStr1 = len(str1)
    distance = 0
    for i in range(lengthOfStr1):
        if str1[i] != str2[i]:
            distance += 1
    return distance


def main():
    print(hamming_distance("toned", "roses"))


if __name__ == "__main__":
    main()
