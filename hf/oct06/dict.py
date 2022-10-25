#!/usr/bin/env python3
# encoding: utf-8
from typing import List


list = [5, 2, 3, 5, 1, 4, -200, 5, 1, 3, 2, 2, 5]


def dictDuplic(li: List) -> List:
    """Returns a sorted list of parameter's deduplicated version"""
    result = []
    for item in li:
        if item not in result:
            result.append(item)
    return sorted(result)


def main():
    print(dictDuplic(list))


if __name__ == "__main__":
    main()
