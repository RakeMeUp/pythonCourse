#!/usr/bin/env python3
# encoding: utf-8
import requests


def main():
    url = "https://python.org"
    r = requests.get(url)
    html = r.text
    print(html[:-10])


if __name__ == "__main__":
    main()
