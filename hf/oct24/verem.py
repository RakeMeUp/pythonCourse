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


class Sor:
    def __init__(self) -> None:
        self._data = []

    def enQ(self, value):
        self._data.append(value)

    def deQ(self):
        if self.meret() == 0:
            return None
        return self._data.pop(0)

    def ures(self):
        return len(self._data) == 0

    def meret(self):
        return len(self._data)

    def __str__(self) -> str:
        return str(self._data)


def veremSteps():
    v = Verem()
    print(v)
    print(v.ures())
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)
    print(v.meret())
    print(v.ures())
    x = v.kivesz()
    print(x)
    print(v)
    v.kivesz()
    v.kivesz()
    x = v.kivesz()
    print(x)


def sorSteps():
    v = Sor()
    print(v)
    print(v.ures())
    v.enQ(1)
    v.enQ(4)
    v.enQ(5)
    print(v)
    print(v.meret())
    print(v.ures())
    x = v.deQ()
    print(x)
    print(v)
    v.deQ()
    v.deQ()
    x = v.deQ()
    print(x)


def main():
    print("Sor:")
    sorSteps()
    print("\nVerem:")
    veremSteps()


if __name__ == "__main__":
    main()
