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

    sizes = defaultdict(int)
    PATH = []

    for item in data:
        cmds = item.split(" ")

        if cmds[1] == "cd":
            if cmds[2] == "..":
                PATH.pop()
            else:
                PATH.append(cmds[2])

        elif cmds[1] == "ls" or cmds[0] == "dir":
            continue
        else:
            for i in range(len(PATH) + 1):
                directory = "/".join(PATH[:i])
                sizes[directory] += int(cmds[0])

    _MAX = 100000
    _sizes = list(sizes.values())
    _sizes.sort()

    res = 0
    for size in _sizes:
        if size <= _MAX:
            res += size

    return res
    # for item in data:
    #     if "$ cd" in item and ".." not in item:
    #         _dir = item.split(" ")[2]
    #     elif "$ ls" in item or ".." in item:
    #         continue
    #     else:
    #         if not contains_dir[_dir]:
    #             contains_dir[_dir] = False

    #         if "dir" not in item:
    #             dirs[_dir].append(int(item.split(" ")[0]))
    #         else:
    #             dirs[_dir].append(item)
    #         pieces = item.split(" ")

    #         if pieces[0].isdigit():
    #             sizes[_dir] = sizes[_dir] + int(pieces[0])
    #         else:
    #             contains_dir[_dir] = True

    # print(dirs)
    # print(sizes)
    # print(contains_dir)

    # print(contains_dir.items())
    # print(len([x for x in list(contains_dir.values()) if x == False]))

    # while True in list(contains_dir.values()):
    #     print(len([x for x in list(contains_dir.values()) if x == False]))

    #     for key, value in dirs.items():
    #         if not all(isinstance(x, int) for x in value):
    #             for val in value:
    #                 if isinstance(val, str):
    #                     _p = val.split(" ")

    #                     if contains_dir[_p[1]] is False:
    #                         i = dirs[key].index(val)
    #                         dirs[key][i] = sizes[_p[1]]

    #                         if all(isinstance(x, int) for x in dirs[key]):
    #                             contains_dir[key] = False
    #                             sizes[key] = sum(dirs[key])
    # # print(len([x for x in list(contains_dir.values()) if x == False]))

    # total = defaultdict(int)
    # k = list(dirs.keys())
    # k.reverse()

    # for key in k:
    #     if not all(isinstance(x, int) for x in dirs[key]):
    #         print(dirs[key], key)
    #         print(dirs["vgh"])
    #     if not sum(dirs[key]):
    #         continue
    #     else:
    #         total[key] = sum(dirs[key])

    # _sizes = list(total.values())
    # _sizes.sort()

    # result = 0
    # for i in _sizes:
    #     if result + i < 100000:
    #         result += i
    #     else:
    #         break

    # return result


def part2(data):
    """Solve part 2."""

    sizes = defaultdict(int)
    PATH = []

    for item in data:
        cmds = item.split(" ")

        if cmds[1] == "cd":
            if cmds[2] == "..":
                PATH.pop()
            else:
                PATH.append(cmds[2])

        elif cmds[1] == "ls" or cmds[0] == "dir":
            continue
        else:
            for i in range(len(PATH) + 1):
                directory = "/".join(PATH[:i])
                sizes[directory] += int(cmds[0])

    _MAX = 100000
    _sizes = list(sizes.values())
    _sizes.sort()
    _sizes.pop()

    TOTAL_AVAILABLE = 70000000
    REQUIRED = 30000000

    NEED_TO_DELETE = REQUIRED - (TOTAL_AVAILABLE - _sizes[-1])

    for size in _sizes:
        if size >= NEED_TO_DELETE:
            return size


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
