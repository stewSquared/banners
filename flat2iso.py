#! /usr/bin/python
from itertools import starmap
import sys


def fresh_grid(size):
    height, width = size
    return ([[' '] * 2 * (width + 1)] +
            [['_'] * (2*width + 1) + [' '] for _ in range(height)])


def pop(pos, grid):
    row, col = pos
    grid[row][col*2 + 1 : col*2 + 5] = list(r"/\\\ "[:-1])
    grid[row + 1][col*2 : col*2 + 4] = list(r"\///")
    return grid


def to_str(grid):
    return '\n'.join(starmap(lambda n, line: ' '*n + line,
                             enumerate(''.join(line) for line in grid)))


def from_file(filename):
    with open(filename) as f:
        lines = []
        line = next(f)
        lines.append(line)
        width = len(line)
        for line in f:
            lines.append(line)
        height = len(lines)

    size = (height, width)
    grid = fresh_grid(size)
    for row, line in enumerate(lines):
        for col, block in list(enumerate(line))[::-1]:
            if block == 'X':
                pos = (row, col)
                pop(pos, grid)
    return to_str(grid)



if __name__ == '__main__':
    print(from_file(sys.argv[1]))

