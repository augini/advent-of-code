# aoc_template.py
import pathlib
import sys
from collections import defaultdict


def parse(puzzle_input, type=1, seperator="\n"):
    if type == 1:
        return list(puzzle_input.split())
    elif type == 2:
        return list(puzzle_input.split(seperator))
    elif type == 3:
        return list(puzzle_input.strip().split(seperator))


def part1(data):
    """Solve part 1."""
    indeces = []
    empty_rows, empty_cols = [], []

    for row_i, row in enumerate(data):
        for i, char in enumerate(row):
            if char == "#":
                indeces.append((row_i, i))

    for ind, row in enumerate(data):
        if len(row.replace(".", "")) == 0:
            empty_rows.append(ind)

    vertical = defaultdict(int)
    for row in data:
        for ind, char in enumerate(row):
            if not vertical[ind]:
                vertical[ind] = 0

            if char == "#":
                vertical[ind] += 1

    for key, val in vertical.items():
        if val == 0:
            empty_cols.append(key)

    for i, index in enumerate(indeces):
        count_col = 0
        for empty_col in empty_cols:
            if empty_col < index[1]:
                count_col += 1

        count_row = 0
        for empty_row in empty_rows:
            if empty_row < index[0]:
                count_row += 1

        indeces[i] = (index[0] + count_row, index[1] + count_col)

    sm = 0
    length = len(indeces)

    for i in range(length):
        for j in range(i + 1, length):
            temp = abs(indeces[j][0] - indeces[i][0]) + abs(
                indeces[j][1] - indeces[i][1]
            )

            sm += temp
    return sm


def part2(data):
    """Solve part 2."""
    indeces = []
    empty_rows, empty_cols = [], []

    for row_i, row in enumerate(data):
        for i, char in enumerate(row):
            if char == "#":
                indeces.append((row_i, i))

    for ind, row in enumerate(data):
        if len(row.replace(".", "")) == 0:
            empty_rows.append(ind)

    vertical = defaultdict(int)
    for row in data:
        for ind, char in enumerate(row):
            if not vertical[ind]:
                vertical[ind] = 0

            if char == "#":
                vertical[ind] += 1

    for key, val in vertical.items():
        if val == 0:
            empty_cols.append(key)

    for i, index in enumerate(indeces):
        count_col = 0
        for empty_col in empty_cols:
            if empty_col < index[1]:
                count_col += 999999

        count_row = 0
        for empty_row in empty_rows:
            if empty_row < index[0]:
                count_row += 999999

        indeces[i] = (index[0] + count_row, index[1] + count_col)

    sm = 0
    length = len(indeces)

    for i in range(length):
        for j in range(i + 1, length):
            temp = abs(indeces[j][0] - indeces[i][0]) + abs(
                indeces[j][1] - indeces[i][1]
            )

            sm += temp
    return sm


def solve(puzzle_input):
    # Solve the puzzle for the given input.
    # parse the given input
    data = parse(puzzle_input, 2)

    # get the solutions for each problem
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
