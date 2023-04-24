"""Add the semicolon at the end of every line"""

import sys

file = sys.argv[1]
lines = []
with open(file) as fh:
    for line in fh:
        line = line.replace("'None'", 'NULL')
        lines.append(line.strip() + ';' + '\n')

with open(file, 'w') as fh:
    fh.writelines(lines)
