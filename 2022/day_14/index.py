# aoc_template.py

import pathlib
import sys
from collections import defaultdict
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


def part1(data):
    """Solve part 1."""
    coor = defaultdict(set)
    coor["sand"] = set()

    left_bound, right_bound = math.inf, -math.inf

    for item in data:
        parts = item.strip().replace(" ", "").split("->")
        i = 1
        length = len(parts)

        while i < length:
            curr = parts[i].split(",")
            prev = parts[i - 1].split(",")

            # print(curr, prev)
            curr[0], curr[1] = int(curr[0]), int(curr[1])
            prev[0], prev[1] = int(prev[0]), int(prev[1])
            # print(curr, prev)

            temp_min = min(curr[0], prev[0])
            temp_max = max(curr[0], prev[0])

            if temp_min < left_bound:
                left_bound = temp_min
            if temp_max > right_bound:
                right_bound = temp_max

            # populate the dictionary with the rock coordinates
            if curr[0] == prev[0]:
                _min = min(curr[1], prev[1])
                _max = max(curr[1], prev[1])

                for x in range(_min, _max + 1):
                    coor["rock"].add((prev[0], x))

            elif curr[1] == prev[1]:
                _min = min(curr[0], prev[0])
                _max = max(curr[0], prev[0])

                for x in range(_min, _max + 1):
                    coor["rock"].add((x, prev[1]))
            else:
                if i == 1:
                    coor["rock"].add((prev[0], prev[1]))

                coor["rock"].add((curr[0], curr[1]))
            i += 1

    floor = 2 + max(r[1] for r in coor["rock"])

    for x in range(left_bound - 2000, right_bound + 2000):
        coor["rock"].add((x, floor))

    part_one = False
    for t in range(1000000):
        x, y = 500, 0
        while True:
            left, middle, right = (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)
            # print(x, y)

            if y + 1 >= floor and (not part_one):
                part_one = True
                print(t)

            if middle not in coor["rock"]:
                y += 1

            elif left not in coor["rock"]:
                x -= 1
                y += 1

            elif right not in coor["rock"]:
                x += 1
                y += 1
            else:
                break
        if x == 500 and y == 0:
            break

        coor["rock"].add((x, y))
    return t + 1


def part2(data):
    """Solve part 2."""


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
