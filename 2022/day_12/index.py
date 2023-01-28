# aoc_template.py

import pathlib
import sys
from collections import deque


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
    heightmap = []

    for item in data:
        temp = []
        for char in item:
            temp.append(char)
        heightmap.append(temp)
        temp = []

    q = deque([])
    q.append(((0, 0), heightmap[0][1], set()))

    col, row = len(heightmap) - 1, len(heightmap[0]) - 1
    complete = []

    while q:
        curr = q.popleft()
        coor, path, history = curr[0], curr[1], curr[2]

        if path[-1] == "{":
            complete.append(path)

        curr_char = heightmap[coor[0]][coor[1]]

        if coor[0] < col:
            down_char = heightmap[coor[0] + 1][coor[1]]
            next = (coor[0] + 1, coor[1])

            if ord(down_char) - ord(curr_char) <= 1 and next not in history:
                history.add(next)
                q.append((next, path + down_char, history))

        if coor[1] < row:

            right_char = heightmap[coor[0]][coor[1] + 1]
            next = (coor[0], coor[1] + 1)

            if ord(right_char) - ord(curr_char) <= 1 and next not in history:
                history.add(next)
                q.append((next, path + right_char, history))

        if coor[1] > 0:

            left_char = heightmap[coor[0]][coor[1] - 1]
            next = (coor[0], coor[1] - 1)

            if ord(left_char) - ord(curr_char) <= 1 and next not in history:
                history.add(next)
                q.append((next, path + left_char, history))

        if coor[0] > 0:

            up_char = heightmap[coor[0] - 1][coor[1]]
            next = (coor[0] - 1, coor[1])

            if ord(up_char) - ord(curr_char) <= 1 and next not in history:
                history.add(next)
                q.append((next, path + up_char, history))

    # print(complete)
    for path in complete:
        print(path)
        print(len(path))


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
