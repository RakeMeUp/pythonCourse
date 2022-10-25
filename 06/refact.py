#!/usr/bin/env python3
# encoding: utf-8

def main():
    f1 = open("text.txt", 'r')
    f2 = open("out", 'w')
    for line in f1:
        f2.write(line)
    f1.close()
    f2.close()


if __name__ == "__main__":
    main()
