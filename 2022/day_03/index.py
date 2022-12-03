# aoc_template.py

import pathlib
import sys


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
    common = []

    score = 0
    for i in data:
        l = len(i) // 2
        part1, part2 = i[:l], i[l:]

        for char in part1:
            if char in part2:
                common.append(char)
                break
        # print(part1, part2)
    # print(common)
    for c in common:
        ascii = ord(c)
        if ascii >= 65 and ascii <= 90:
            temp = 27 + (ascii - 65)
        elif ascii >= 97:
            temp = ascii - 96

        # print(temp)
        score += temp
    return score


def part2(data):
    """Solve part 2."""
    common = []

    score = 0
    length = len(data)

    for i in range(0, length - 1, 3):
        for char_1 in data[i]:
            if char_1 in data[i + 1] and char_1 in data[i + 2]:
                common.append(char_1)
                break

    for c in common:
        ascii = ord(c)
        if ascii >= 65 and ascii <= 90:
            temp = 27 + (ascii - 65)
        elif ascii >= 97:
            temp = ascii - 96

        # print(temp)
        score += temp
    return score


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
