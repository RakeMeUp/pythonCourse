#!/usr/bin/env python3
# encoding: utf-8

def main():
    a = [1, 2, 3]
    b = a[:]  # or  b = a.copy()

    x = a.pop(0)

    c = [2, 3]
    a.append(c)

    a.extend(c)  # a+=c


if __name__ == "__main__":
    main()
