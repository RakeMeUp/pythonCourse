#!/usr/bin/env python3
# encoding: utf-8

import requests

def main():
    req = requests.get("https://jsonip.com/")
    print(req.json()["ip"])

if __name__ == "__main__":
    main()