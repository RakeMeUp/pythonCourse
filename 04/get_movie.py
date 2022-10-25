#!/usr/bin/env python3
# encoding: utf-8
def get_movie_info():
    # adat lekeres
    return ("moviename", 'year', 'imdbRate')


def main():
    (title, year, score) = get_movie_info()
    print(title, year, score)


if __name__ == "__main__":
    main()
