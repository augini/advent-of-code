# aoc_template.py

import pathlib
import sys
from collections import defaultdict
import math


def parse(puzzle_input, type=1, seperator="\n"):
    # Parses the input
    if type == 1:
        return list(puzzle_input.split())
    elif type == 2:
        return list(puzzle_input.split(seperator))
    elif type == 3:
        return list(puzzle_input.strip().split(seperator))


def part1(data):
    """Solve part 1."""
    data = [x for x in data if len(x)]
    maps = defaultdict(list)
    seeds = []

    curr = ""

    for line in data:
        if line.startswith("seeds:"):
            line = line.strip().split("seeds:")[1].split(" ")
            seeds = [int(x) for x in line if len(x)]
        elif "-" in line:
            curr = line.replace(" map", "").replace(":", "")
        else:
            line = line.split()
            line = [int(x) for x in line]

            destination = range(line[0], line[0] + line[2])
            source = range(line[1], line[1] + line[2])

            maps[curr].append((destination, source))

    mn = math.inf

    for seed in seeds:
        next = seed
        for key in maps.keys():
            for mapping in maps[key]:
                if next in mapping[1]:
                    ind = mapping[1].index(next)
                    next = mapping[0][0] + ind
                    break
        if next < mn:
            mn = next
    return mn


def part2(data):
    """Solve part 1."""
    data = [x for x in data if len(x)]
    maps = defaultdict(list)
    seeds = []

    curr = ""

    for line in data:
        if line.startswith("seeds:"):
            line = line.strip().split("seeds:")[1].split(" ")
            seeds = [int(x) for x in line if len(x)]

        elif "-" in line:
            curr = line.replace(" map", "").replace(":", "")
        else:
            line = line.split()
            line = [int(x) for x in line]

            destination = range(line[0], line[0] + line[2])
            source = range(line[1], line[1] + line[2])

            maps[curr].append((destination, source))

    mn = math.inf

    for i in range(0, len(seeds), 2):
        for seed in range(seeds[i], seeds[i] + seeds[i + 1]):
            next = seed
            for key in maps.keys():
                for mapping in maps[key]:
                    if next in mapping[1]:
                        ind = mapping[1].index(next)
                        next = mapping[0][0] + ind
                        break
            if next < mn:
                mn = next
    return mn


def solve(puzzle_input):
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
