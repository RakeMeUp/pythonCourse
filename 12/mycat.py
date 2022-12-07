#!/usr/bin/env python3
# encoding: utf-8
import sys

def cat(fname:sys)-> None:
    try:
        f = open(fname)
        content = f.read().strip()
        f.close()
        print(content)
    except FileNotFoundError as e:
        print(e)

def main():
    args= sys.argv[1:]
    for fname in args:
        cat(fname)
    

if __name__ == "__main__":
    main()