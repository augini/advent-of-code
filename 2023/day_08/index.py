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
    """Solve part 1."""

    maps = defaultdict(dict)
    instruction = [*data[0]]
    data = data[2:]

    for line in data:
        parts = line.split(" ")
        l = parts[2].replace("(", "").replace(",", "")
        r = parts[3].replace(")", "")
        maps[parts[0]]["L"] = l
        maps[parts[0]]["R"] = r

    curr = "AAA"
    length = len(instruction)

    counter = 1
    while curr != "ZZZ":
        i = 0
        while i < length:
            dir = instruction[i]
            curr = maps[curr][dir]
            if curr == "ZZZ":
                break
            counter += 1
            i += 1
        i = 0
    return ""


def part2(data):
    """Solve part 2."""
    maps = defaultdict(dict)
    instruction = [*data[0]]
    data = data[2:]

    starting_nodes = []

    for line in data:
        parts = line.split(" ")

        if parts[0][2] == "A":
            starting_nodes.append(parts[0])

        l = parts[2].replace("(", "").replace(",", "")
        r = parts[3].replace(")", "")

        maps[parts[0]]["L"] = l
        maps[parts[0]]["R"] = r

    length = len(instruction)
    ending_nodes = []
    ending_in_z = []
    counter = 0

    while True:
        i = 0
        while i < length:
            dir = instruction[i]
            for node in starting_nodes:
                curr = maps[node][dir]
                if curr[2] == "Z":
                    ending_in_z.append(curr)
                ending_nodes.append(curr)

            if len(ending_in_z) == len(starting_nodes):
                return counter + 1

            starting_nodes = ending_nodes
            ending_nodes, ending_in_z = [], []
            i += 1
            counter += 1


def solve(puzzle_input):
    # Solve the puzzle for the given input.

    data = parse(puzzle_input, 2)

    # get the solutions for each problem
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    #  print(sys.argv)
    for path in sys.argv[1:]:
        #   print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
