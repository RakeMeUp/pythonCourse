#!/usr/bin/env python3
# encoding: utf-8
import json
from pprint import pprint

def main():
    fname = "person.json"
    f = open(fname)
    
    d = json.load(f)
    print(type(d))
    print(d["age"])
    pprint(d)

    f.close()

if __name__ == "__main__":
    main()