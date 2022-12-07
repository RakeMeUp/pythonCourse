#!/usr/bin/env python3
# encoding: utf-8
from is_prime import is_prime
import time

def main():
    st = time.time()
    for x in range(100):
        if is_prime(x):
            print(f"{x}, ", end="")
    print("")
    et = time.time()
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')

if __name__ == "__main__":
    main()