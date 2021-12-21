"""The entry point."""

import timeit

from easy.palindrome_number import *


def main():
    time_it()


def time_it():
    res = timeit.timeit(stmt='test()', globals=globals())
    print(res)


if __name__ == '__main__':
    main()
