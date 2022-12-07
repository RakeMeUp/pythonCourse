#!/usr/bin/env python3
# encoding: utf-8

def subset_sum(numbers, target, partial=[]):
    s = sum(partial)
    cache = []

    # check if the partial sum is equals to target
    if s == target:
        if len(partial) == 6:
            cache.append(partial)

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        subset_sum(remaining, target, partial + [n])


def main():
    print(subset_sum(range(1,46),90))
    

if __name__ == "__main__":
    main()