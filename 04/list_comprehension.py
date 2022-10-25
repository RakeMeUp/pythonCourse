#!/usr/bin/env python3
# encoding: utf-8

def main():
    nums = [1, 2, 3, 4, 5]
    # like map
    squares = [n**2 for n in nums]
    print(squares)
    small = [n for n in nums if n <= 2]
    print(small)


if __name__ == "__main__":
    main()
