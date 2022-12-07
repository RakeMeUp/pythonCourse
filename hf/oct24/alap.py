#!/usr/bin/env python3
# encoding: utf-8
import sys
from os import path

TEMPLATE_PY = '''#!/usr/bin/env python3
# encoding: utf-8

def main():

if __name__ == "__main__":
    main()
'''
TEMPLATE_JS = '''console.log("hello");'''
TEMPLATE_PHP = '''<?php

'''

def main():
    if sys.argv[1] == "py":
        if path.exists("start.py"):
            print('already exists')
            return
        with open('start.py', 'w') as f:
            print('start.py has been created')
            f.write(TEMPLATE_PY)

    elif sys.argv[-1] == "js":
        if path.exists("start.js"):
            print('already exists')
            return
        with open('start.js', 'w') as f:
            print('start.js has been created')
            f.write(TEMPLATE_JS)
            
    elif sys.argv[1] == "php":
        if path.exists("start.php"):
            print('already exists')
            return
        with open('start.php', 'w') as f:
            print('start.php has been created')
            f.write(TEMPLATE_PHP)

if __name__ == "__main__":
    main()