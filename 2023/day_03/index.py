# aoc_template.py

import pathlib
import sys
import re
from collections import defaultdict


def parse(puzzle_input, type=1, seperator="\n"):
    # Parses the input

    if type == 1:
        return list(puzzle_input.split())
    elif type == 2:
        return list(puzzle_input.split(seperator))
    elif type == 3:
        return list(puzzle_input.strip().split(seperator))


def contains_symbol(top, front, back, bottom):
    return any(len(side.replace(".", "")) > 0 for side in (top, front, back, bottom))


def is_star(char):
    return char == "*"


def part1(data):
    """Solve part 1."""
    valid_numbers = []

    for row, line in enumerate(data):
        num = ""
        top, bottom, front, back = "", "", "", ""

        for ind, char in enumerate(line):
            if char.isdigit():
                is_first = len(num) == 0
                is_last = ind == len(line) - 1

                # get element in front
                if ind > 0 and is_first:
                    front = data[row][ind - 1]

                # get top row
                if row > 0:
                    top_row = data[row - 1]

                    # get top diagonal left
                    if ind > 0 and is_first:
                        top = top + top_row[ind - 1]

                    top = top + top_row[ind]

                # get bottom row
                if row < len(data) - 1:
                    bottom_row = data[row + 1]

                    # get the bottom diagonal left
                    if ind > 0 and is_first:
                        bottom = bottom + bottom_row[ind - 1]
                    bottom = bottom + bottom_row[ind]

                num = num + char

                # get the number at the end of the current line
                if is_last and contains_symbol(top, front, back, bottom):
                    valid_numbers.append(int(num))

            elif num:
                # get the element next in current row
                back = char

                # get the bottom diagonal right
                if row < len(data) - 1:
                    bottom = bottom + data[row + 1][ind]

                # get the top diagonal right
                if row > 0:
                    top = top + data[row - 1][ind]

                if contains_symbol(top, front, back, bottom):
                    valid_numbers.append(int(num))

                top, bottom, front, back = "", "", "", ""
                num = ""

    return sum(valid_numbers)


def part2(data):
    """Solve part 2."""
    nums_arouns_str = defaultdict(list)

    for row, line in enumerate(data):
        num = ""
        star_indices = []

        for ind, char in enumerate(line):
            if char.isdigit():
                is_first = len(num) == 0
                is_last = ind == len(line) - 1

                # check element in front
                if ind > 0 and is_first and is_star(data[row][ind - 1]):
                    star_indices.append((row, ind - 1))

                # check top row
                if row > 0:
                    top_row = data[row - 1]

                    # check top diagonal left
                    if ind > 0 and is_first and is_star(top_row[ind - 1]):
                        star_indices.append((row - 1, ind - 1))

                    if is_star(top_row[ind]):
                        star_indices.append((row - 1, ind))

                # check bottom row
                if row < len(data) - 1:
                    bottom_row = data[row + 1]

                    # check the bottom diagonal left
                    if ind > 0 and is_first and is_star(bottom_row[ind - 1]):
                        star_indices.append((row + 1, ind - 1))

                    if is_star(bottom_row[ind]):
                        star_indices.append((row + 1, ind))

                num = num + char

                # check the number at the end of the current line
                if is_last:
                    for x, y in star_indices:
                        nums_arouns_str[(x, y)].append(int(num))

            elif num:
                # check the element next in current row
                if is_star(char):
                    star_indices.append((row, ind))

                # check the bottom diagonal right
                if row < len(data) - 1 and is_star(data[row + 1][ind]):
                    star_indices.append((row + 1, ind))

                # check the top diagonal right
                if row > 0 and is_star(data[row - 1][ind]):
                    star_indices.append((row - 1, ind))

                for x, y in star_indices:
                    nums_arouns_str[(x, y)].append(int(num))

                num = ""
                star_indices = []

    return sum(nums[0] * nums[1] for nums in nums_arouns_str.values() if len(nums) == 2)


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
