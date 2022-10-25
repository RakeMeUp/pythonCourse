#!/usr/bin/env python3
# encoding: utf-8

class EmptyClass:
    pass


class MyClass:
    def hello(self):
        return "hello"


class Hello:
    def createName(self, name):
        self.name = name

    def displayName(self):
        return self.name


def main():
    obj = EmptyClass()
    ob1 = MyClass()
    ob2 = Hello()
    print(ob1.hello())
    ob2.createName("Kutya")
    print(ob2.displayName())


if __name__ == "__main__":
    main()
