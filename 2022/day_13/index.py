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


def check(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif left == right:
            return 0
        else:
            return -1
    elif isinstance(left, int) and isinstance(right, list):
        return check([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return check(left, [right])
    else:
        # TODO: checkout the implementation with zip
        l1, l2 = len(left), len(right)
        count = 0
        while count < l1 and count < l2:
            result = check(left[count], right[count])
            if result == 1:
                return 1
            elif result == -1:
                return -1
            count += 1

        if count >= l1 and count < l2:
            return 1
        elif count >= l2 and count < l1:
            return -1


def part1(data):
    """Solve part 1."""
    l = len(data)
    _sum = 0

    for i in range(0, l, 3):
        left, right = eval(data[i]), eval(data[i + 1])
        res = check(left, right)
        if res == 1:
            _sum += (i // 3) + 1
    return _sum


# Space Complexity:
# Time Complexity:


def part2(data):
    """Solve part 2."""
    i1, i2 = 1, 1
    data = list(filter(lambda x: x, data))

    # append items that come before [[2]]
    for item in data:
        # get lines that are less than [[2]] only
        res_two = check(eval(item), [[2]])

        # get lines that are less [[6]]
        res_six = check(eval(item), [[6]])

        if res_six == 1:
            i2 += 1
        if res_two == 1:
            i1 += 1

    # length += 1
    # i1 = length

    # append items that come after [[2]] and before [[6]]
    # for item in data:
    #     _res = check([[2]], eval(item))
    #     res = check(eval(item), [[6]])
    #     if res == 1 and _res == 1:
    #         length += 1

    # length += 1
    # i2 = length

    return i1 * (i2 + 1)


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
