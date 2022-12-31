import itertools
import sys

HELP: str = 'Use the two file pathes in the arguments'

try:
    first_path, second_path = sys.argv[1:]
except ValueError:
    print(HELP)
    sys.exit(1)

with open(first_path) as fh1, open(second_path) as fh2:
    for line1, line2 in itertools.zip_longest(fh1, fh2):
        line1: str = line1.strip().replace(' Null ', ' NULL ')
        line2: str = line1.strip().replace(' Null ', ' NULL ')
        if line1 != line2:
            sys.exit(1)

sys.exit(0)
