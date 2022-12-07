#!/usr/bin/env python3
# encoding: utf-8


def main():
    print(sorted(["1", "5552", "34", "456"], key=len))
    # print([chr(x) for x in range(100)])
    print(sorted(["Cc", "BB", "aa", "zz"], key=str.lower))
    print(
        sorted(
            ["wa", "xc", "zb", "yd"],
        )
    )


if __name__ == "__main__":
    main()
