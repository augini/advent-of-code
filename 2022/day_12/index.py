# aoc_template.py

import pathlib
import sys
from collections import deque
import math


def parse(puzzle_input, type=1, seperator="\n"):
    # Parses the input

    #  print(puzzle_input)
    if type == 1:
        return list(puzzle_input.split())
    elif type == 2:
        return list(puzzle_input.split(seperator))
    elif type == 3:
        return list(puzzle_input.strip().split(seperator))


def part(data, part):
    """Solve parts 1 and 2"""
    grid = []

    for line in data:
        temp = []
        for char in line:
            temp.append(char)
        grid.append(temp)

    R = len(grid)
    C = len(grid[0])

    V = [[0 for _ in range(C)] for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if grid[r][c] == "S":
                V[r][c] = 1
            elif grid[r][c] == "E":
                V[r][c] = 26
            else:
                V[r][c] = ord(grid[r][c]) - ord("a") + 1

    q = deque([])

    for r in range(R):
        for c in range(C):
            if part == 1:
                if grid[r][c] == "S":
                    q.append(((r, c), 0))
            elif part == 2:
                if grid[r][c] == "a":
                    q.append(((r, c), 0))

    visited = set()

    while q:
        (r, c), count = q.popleft()
        if (r, c) in visited:
            continue

        visited.add((r, c))

        if grid[r][c] == "E":
            return count

        for y, x in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ry = r + y
            cx = c + x

            if 0 <= ry < R and 0 <= cx < C and V[ry][cx] <= 1 + V[r][c]:
                q.append(((ry, cx), count + 1))

    return 1


def solve(puzzle_input):
    # Solve the puzzle for the given input.
    # parse the given input
    data = parse(puzzle_input, 2)

    # get the solutions for each problem
    solution1 = part(data, 1)
    solution2 = part(data, 2)

    return solution1, solution2


if __name__ == "__main__":
    #  print(sys.argv)
    for path in sys.argv[1:]:
        #   print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
