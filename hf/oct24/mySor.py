#!/usr/bin/env python3
# encoding: utf-8


class Verem:
    def __init__(self) -> None:
        self._data = []

    def betesz(self, value):
        self._data.append(value)

    def kivesz(self):
        if self.meret() == 0:
            return None
        return self._data.pop()

    def ures(self):
        return len(self._data) == 0

    def meret(self):
        return len(self._data)

    def __str__(self) -> str:
        return str(self._data)


class mySor:
    def __init__(self) -> None:
        self._dataOut = Verem()
        self._dataIn = Verem()

    def append(self, value):
        self._dataIn.betesz(value)

    def popleft(self):
        if self._dataIn.meret() == 0:
            return None
        while self._dataIn.meret() != 0:
            self._dataOut.betesz(self._dataIn.kivesz())
        return self._dataOut.kivesz()

    def is_empty(self):
        return self._dataIn.meret() == 0 and self._dataOut.meret() == 0

    def size(self):
        return self._dataIn.meret() + self._dataOut.meret()

    def __str__(self) -> str:
        return str(self._dataIn)


def main():
    v = mySor()
    print(v)
    print(v.is_empty())
    v.append(1)
    v.append(4)
    v.append(5)
    print(v)
    print(v.size())
    print(v.is_empty())
    x = v.popleft()
    print(x)
    print(v)
    v.popleft()
    v.popleft()
    x = v.popleft()
    print(x)


if __name__ == "__main__":
    main()
