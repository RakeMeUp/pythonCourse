#!/usr/bin/env python3
# encoding: utf-8
import re


def main():

    f = open("csv.txt", "r")
    for sor in f:
        if re.match(".*j.*s.*u.*n.*", sor):
            print(sor.split(",")[0])
    f.close()


if __name__ == "__main__":
    main()
