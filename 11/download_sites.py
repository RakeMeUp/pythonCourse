#!/usr/bin/env python3
# encoding: utf-8
import urllib.request
import get_page


def htmll():
    url = "https://www.python.org/"
    response = urllib.request.urlopen(url)
    raw = response.read()
    print(type(raw))
    print(raw)
    html = raw.decode("utf-8")
    print(type(html))
    print(html)


def main():
    url = "https://www.python.org/"
    print(get_page.get_page(url))


if __name__ == "__main__":
    main()
