#!/usr/bin/env python3
# encoding: utf-8
import os


def main():
    url = "https://m.media-amazon.com/images/M/MV5BZmU5ZDE5NTItN2I1YS00ZmFmLTk3YTgtNzQwOGNkYzFjOWRkXkEyXkFqcGdeQXVyNzU1NzE3NTg@._V1_QL75_UX500_CR0,47,500,281_.jpg"
    cmd = f"wget '{url}' -0 wallpaper.jpg"
    os.system(cmd)
    print(cmd)


if __name__ == "__main__":
    main()
