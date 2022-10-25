#!/usr/bin/env python3
# encoding: utf-8

def main():
    t = (2, 3, 4, 6)
    # cant directly change like t[0] = 1
    t1 = (1)
    print(t1)
    (x, y) = (3, 5)
    print(x, y)
    # swap value:
    (x, y) = (y, x)
    print(x, y)


if __name__ == "__main__":
    main()
