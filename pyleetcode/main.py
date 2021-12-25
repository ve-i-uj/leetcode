"""The entry point."""

import timeit

from easy.roman_to_integer import test


def main():
    test()


def time_it():
    res = timeit.timeit(stmt='test()', globals=globals())
    print(res)


if __name__ == '__main__':
    main()
