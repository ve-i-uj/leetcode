"""The entry point."""

import timeit


def test():
    pass


def main():
    time_it()


def time_it():
    res = timeit.timeit(stmt='test()', globals=globals())
    print(res)


if __name__ == '__main__':
    main()
