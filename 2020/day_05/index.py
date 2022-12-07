# aoc_template.py

import pathlib
import sys
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
    _min, _max = 0, 127
    curr = 0
    result = 0

    for item in data:
        curr = 0
        _min, _max = 0, 127
        first, second = item[0:7], item[7:]

        for char in first:
            curr = (_min + _max) // 2
            if char == "F":
                _max = curr
            elif char == "B":
                _min = curr + 1

        _min, _max = 0, 7
        second += " "

        for char in second:
            col = (_min + _max) / 2
            if char == "L":
                _max = math.floor(col)
            elif char == "R":
                _min = math.ceil(col)
        temp = (curr * 8) + col
        # print(temp)
        if temp > result:
            result = temp

    return result


def part2(data):
    """Solve part 2."""
    """Solve part 1."""
    _min, _max = 0, 127
    curr = 0

    ids = []

    for item in data:
        curr = 0
        _min, _max = 0, 127
        first, second = item[0:7], item[7:]

        for char in first:
            curr = (_min + _max) // 2
            if char == "F":
                _max = curr
            elif char == "B":
                _min = curr + 1

        _min, _max = 0, 7
        second += " "

        for char in second:
            col = (_min + _max) / 2
            if char == "L":
                _max = math.floor(col)
            elif char == "R":
                _min = math.ceil(col)
        temp = curr * 8 + col
        ids.append(temp)
        # print(temp)

    ids.sort()
    my_id = 0

    for _id in ids:
        if _id + 1 not in ids and _id + 2 in ids:
            my_id = _id + 1
    return my_id


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
