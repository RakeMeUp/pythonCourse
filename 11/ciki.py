#!/usr/bin/env python3
# encoding: utf-8

import requests
import time
import random


def main():
    url = "https://divany.hu/offline/2016/02/03/nagyi_sarok_trendek_cipok_2016/?p=&meno=1&posztbol=1"
    for i in range(100):
        r = requests.get(url)
        html = r.text
        print(".", end="", flush=True)
        # time.sleep(random(int()))
    print()


if __name__ == "__main__":
    main()
