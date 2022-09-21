#!/usr/bin/env python3
# encoding: utf-8

MAX = 10
PI = 3.14159


def hello(name, color, obj):
    print("{0}, {1} az {2}".format(name, color, obj))
    print("{}, {} az {}".format(name, color, obj))
    print("{name}, {color} az {obj}".format(name=name, color=color, obj=obj))
    print(f"{name.capitalize()}, {color} az {obj}")
    print("-" * 20)


def main():
    hello("geza", "kek", "eg")
    hello("julcsi", "piros", "auto")


if __name__ == "__main__":
    main()
