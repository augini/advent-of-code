# aoc_template.py

import pathlib
import sys
from collections import defaultdict, deque
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
    else:
        return "Freestyle"


def part1(data):
    """Solve part 1."""

    stacks = defaultdict(list)
    inst = []

    length = len(data)
    for i in range(length):
        if data[i] == "":
            inst.extend(data[i + 1 :])
            break

        for y in range(len(data[i])):
            curr = data[i][y]

            if curr != "" and curr != " " and curr != "[" and curr != "]":
                step = math.ceil(y / 3)

                if ord(curr) < 64:
                    temp = stacks[step]
                    del stacks[step]
                    stacks[int(curr)] = list(reversed(temp))
                else:
                    stacks[step].append(curr)

    for item in inst:
        items = item.split(" ")
        one, two, three = int(items[1]), int(items[3]), int(items[5])

        for i in range(one):
            temp = stacks[two].pop()
            stacks[three].append(temp)

    result = ""
    l = len(stacks)

    for key in range(1, l + 1):
        temp = stacks[key].pop()
        result += temp

    return "".join(result)


def part2(data):
    """Solve part 2."""
    stacks = defaultdict(list)
    inst = []

    length = len(data)
    for i in range(length):
        if data[i] == "":
            inst.extend(data[i + 1 :])
            break

        for y in range(len(data[i])):
            curr = data[i][y]

            if curr != "" and curr != " " and curr != "[" and curr != "]":
                step = math.ceil(y / 3)

                if ord(curr) < 64:
                    temp = stacks[step]
                    del stacks[step]
                    stacks[int(curr)] = list(reversed(temp))
                else:
                    stacks[step].append(curr)

    for item in inst:
        items = item.split(" ")
        one, two, three = int(items[1]), int(items[3]), int(items[5])

        mv = []
        for i in range(one):
            temp = stacks[two].pop()
            mv.append(temp)
        mv.reverse()
        stacks[three].extend(mv)

    result = ""
    l = len(stacks)

    for key in range(1, l + 1):
        temp = stacks[key].pop()
        result += temp

    return "".join(result)


def solve(puzzle_input):
    # Solve the puzzle for the given input.
    # parse the given input
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
