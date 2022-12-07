#!/usr/bin/env python3
# encoding: utf-8

def main():
    tomb = []
    accumulated = 0

    file = open('./input.txt')
    for sor in file:
        tomb.append([int(num) for num in sor.split()])
    file.close()

    checkSum = sum([max(sor) - min(sor) for sor in tomb])

    for sor in tomb:
        for elso in sor:
            for masodik in sor:
                if elso != masodik and elso % masodik == 0:
                    accumulated += elso / masodik

    print(checkSum)
    print(accumulated)


if __name__ == "__main__":
    main()