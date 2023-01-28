# aoc_template.py

import pathlib
import sys
from collections import defaultdict


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
    nums = []

    for item in data:
        nums.append(int(item))

    l = len(nums)

    for i in nums.copy():
        if i == 0:
            continue
        oldI = nums.index(i)
        temp = nums.pop(oldI)

        if i > 0:
            newI = oldI + i
        elif i < 0:
            newI = (oldI + l - 1) - abs(i)

        if newI >= l:
            newI = newI % l + 1

        first, second = nums[:newI], nums[newI:]
        nums = first + [temp] + second

    # print(nums)

    i = nums.index(0)

    first = ((1000 % l) + nums.index(0)) % 7
    second = ((2000 % l) + nums.index(0)) % 7
    third = ((3000 % l) + nums.index(0)) % 7

    print(nums[first], nums[second], nums[third])


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
