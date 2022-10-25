#!/usr/bin/env python3
# encoding: utf-8

class Container:
    def __init__(self) -> None:
        self._data = []

    def add(self, value):
        self._data.append(value)

    def add_twice(self, value):
        self.add(value)
        self.add(value)

    def __str__(self):
        return "Object Bag (" + str(self._data) + ")"


def main():
    obj = Container()
    obj.add(1)
    obj.add(1)
    obj.add(1)
    obj.add(1)
    print(obj)


if __name__ == "__main__":
    main()
