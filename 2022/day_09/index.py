# aoc_template.py

import pathlib
import sys
from typing import Optional, List


def parse(puzzle_input, type=1, seperator="\n"):
    # Parses the input

    #  print(puzzle_input)
    if type == 1:
        return list(puzzle_input.split())
    elif type == 2:
        return list(puzzle_input.split(seperator))
    elif type == 3:
        return list(puzzle_input.strip().split(seperator))


def update_tail(head, tail, path: Optional[list] = None):
    # 0 -> x, 1 -> y

    row_diff = abs(head[0] - tail[0])
    col_diff = abs(head[1] - tail[1])

    def update_row(head, tail):
        if head[0] > tail[0]:
            tail[0] = head[0] - 1
        else:
            tail[0] = head[0] + 1
        return head, tail

    def update_col(head, tail):
        if head[1] > tail[1]:
            tail[1] = head[1] - 1
        else:
            tail[1] = head[1] + 1
        return head, tail

    # if in the same row
    if row_diff == 2 and col_diff == 0:
        head, tail = update_row(head, tail)

    # if in the same column
    elif col_diff == 2 and row_diff == 0:
        head, tail = update_col(head, tail)

    # not in the same row or col
    elif col_diff >= 2 or row_diff >= 2:

        if row_diff == 1:
            tail[0] = head[0]
            head, tail = update_col(head, tail)

        elif col_diff == 1:
            tail[1] = head[1]
            head, tail = update_row(head, tail)

    if path is not None:
        path.add(tuple(tail))

    return head, tail


def part1(data):
    """Solve part 1."""
    instructions = []
    path = set()

    print(instructions)
    # 0 -> x, 1 -> y
    coor = {"h": [0, 0], "t": [0, 0]}

    # O(n)
    for i in data:
        parts = i.split(" ")
        parts[1] = int(parts[1])

        diff = [0, 0]

        if i[0] == "R":
            diff[0] += 1
        elif i[0] == "L":
            diff[0] -= 1
        elif i[0] == "U":
            diff[1] += 1
        elif i[0] == "D":
            diff[1] -= 1

        # O(m), e.g m = n
        for _ in range(parts[1]):
            coor["h"][0] = coor["h"][0] + diff[0]
            coor["h"][1] = coor["h"][1] + diff[1]

            coor["h"], coor["t"] = update_tail(coor["h"], coor["t"], path)

    return len(path)


# Time complexity -> n * m -> O(n*m)
# Space complexity -> O(n)


def part2(data):
    """Solve part 2."""
    instructions = []
    path = set()

    for item in data:
        parts = item.split(" ")
        parts[1] = int(parts[1])
        instructions.append(parts)

    # 0 -> x, 1 -> y
    coor = {
        "h": [0, 0],
        "t": [0, 0],
        "t2": [0, 0],
        "t3": [0, 0],
        "t4": [0, 0],
        "t5": [0, 0],
        "t6": [0, 0],
        "t7": [0, 0],
        "t8": [0, 0],
        "t9": [0, 0],
    }

    for i in instructions:
        diff = [0, 0]

        if i[0] == "R":
            diff[0] += +1
        elif i[0] == "L":
            diff[0] -= 1
        elif i[0] == "U":
            diff[1] += 1
        elif i[0] == "D":
            diff[1] -= 1

        for _ in range(i[1]):
            coor["h"][0] = coor["h"][0] + diff[0]
            coor["h"][1] = coor["h"][1] + diff[1]

            coor["h"], coor["t"] = update_tail(coor["h"], coor["t"])
            coor["t"], coor["t2"] = update_tail(coor["t"], coor["t2"])
            coor["t2"], coor["t3"] = update_tail(coor["t2"], coor["t3"])
            coor["t3"], coor["t4"] = update_tail(coor["t3"], coor["t4"])
            coor["t4"], coor["t5"] = update_tail(coor["t4"], coor["t5"])
            coor["t5"], coor["t6"] = update_tail(coor["t5"], coor["t6"])
            coor["t6"], coor["t7"] = update_tail(coor["t6"], coor["t7"])
            coor["t7"], coor["t8"] = update_tail(coor["t7"], coor["t8"])
            coor["t8"], coor["t9"] = update_tail(coor["t8"], coor["t9"], path)

    return len(path)


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
