#!/usr/bin/env python3
# encoding: utf-8

MELY_MGHK = 'aáoóuú'
MAGAS_MGHK = 'eéiíöőüű'
words = ["ablak", "erkély", "kisvasút", "magas", "mély", "dfghjk"]


def isZongo(str):
    isMely = any(char in list(MELY_MGHK) for char in str)
    isMagas = any(char in list(MAGAS_MGHK) for char in str)
    if isMely and isMagas:
        return 'vegyes'
    if isMagas:
        return 'magas'
    if isMely:
        return 'mély'
    return 'semmilyen'


def main():
    for word in words:
        print(isZongo(word))


if __name__ == "__main__":
    main()
