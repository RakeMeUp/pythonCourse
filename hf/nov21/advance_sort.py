#!/usr/bin/env python3
# encoding: utf-8


def main():
    data = [
        (1, "Albany", "NY", 162692),
        (3, "Allegany", "NY", 11986),
        (121, "Wyoming", "NY", 8722),
        (123, "Yates", "NY", 5094),
    ]
    print(sorted(data, key=lambda x: x[-1]))

    users = ["10:User1", "80:User2", "100:User3", "00:User4", "75:User4", "45:User5"]
    print(sorted(users, key=lambda x: int(x.split(":")[0])))

    li = [[2, 6], [1, 3], [5, 4]]
    print(sorted(li, key=lambda x: x[1]))


if __name__ == "__main__":
    main()
