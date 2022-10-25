#!/usr/bin/env python3
# encoding: utf-8

def loop(loops: int, debug=False):
    """Simply prints the whole numbers up to 'loops', using the optional 'debug' param, you can observe the loops end and start"""
    if debug:
        print("# Start of loop")
    for n in range(1, loops+1):
        print(str(n) + " ", end="")
    if debug:
        print("\n# End of loop")


def main():
    loop(4, debug=True)


if __name__ == "__main__":
    main()
