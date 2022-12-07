#!/usr/bin/env python3
# encoding: utf-8
from is_prime import is_prime

def main():
    li = [x for x in range(200) if is_prime(x)]
    print(sum(li))

if __name__ == "__main__":
    main()