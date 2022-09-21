#!/usr/bin/env python3
# encoding: utf-8

def listed():
    li = [1, 2, 3]
    for e in li:
        li[e-1] *= 2
    print(li)


def main():
    s = "python"
    print(list(s))


if __name__ == "__main__":
    main()
