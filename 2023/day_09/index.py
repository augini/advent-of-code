# aoc_template.py

import pathlib
import sys
from collections import defaultdict


def parse(puzzle_input, type=1, seperator="\n"):
    # Parses the input

    if type == 1:
        return list(puzzle_input.split())
    elif type == 2:
        return list(puzzle_input.split(seperator))
    elif type == 3:
        return list(puzzle_input.strip().split(seperator))


def part1(data):
    sequences = defaultdict(list)

    for ind, line in enumerate(data):
        line = [int(x) for x in line.split() if len(x)]
        sequences[ind].append(line)

        while True:
            diff = []
            for j in range(0, len(line) - 1):
                diff.append(line[j + 1] - line[j])

            sequences[ind].append(diff)

            if diff[0] == 0 and len(set(diff)) == 1:
                # append 0 to the end for the next step
                sequences[ind][-1].append(0)

                break
            line = diff

    total = 0
    for key, val in sequences.items():
        for i in range(len(val) - 2, -1, -1):
            sm = val[i][-1] + val[i + 1][-1]
            if i == 0:
                total += sm

            sequences[key][i].append(sm)

    return total


def part2(data):
    sequences = defaultdict(list)

    for ind, line in enumerate(data):
        line = [int(x) for x in line.split() if len(x)]
        sequences[ind].append(line)

        while True:
            diff = []
            for j in range(0, len(line) - 1):
                diff.append(line[j + 1] - line[j])

            sequences[ind].append(diff)

            if diff[0] == 0 and len(set(diff)) == 1:
                sequences[ind][-1].append(0)
                break

            line = diff

    total = 0

    for key, val in sequences.items():
        for i in range(len(val) - 2, -1, -1):
            sm = val[i][0] - val[i + 1][0]
            if i == 0:
                total += sm

            sequences[key][i].insert(0, sm)

    return total


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
