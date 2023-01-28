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

    push_order = []
    for item in data[0]:
        push_order.append(item)
    push_length = len(push_order)

    print(push_order)
    print(push_length)

    container = [".......", ".......", ".......", "......."]
    stones = [
        "####",
        [".#.", "###", ".#."],
        ["..#,..#,###"],
        ["#", "#", "#", "#"],
        ["##", "##"],
    ]

    stones = ["line", "plus", "L", "cube"]
    rock_number = 0
    push = 0

    coor = defaultdict(set)
    coor["@"] = set()

    x, y = 2, 3

    for i in range(10):
        rock_number = rock_number % 4
        curr_rock = stones[rock_number]

        print(curr_rock)
        rock_number += 1

        if curr_rock == "line":

            while True:
                zones = [(x, y), (x + 1, y), (x + 2, y), ((x + 3, y))]

                push = push % push_length
                curr_push = push_order[push]
                push += 1

                if curr_push == ">" and zones[-1][0] < 6:
                    for z in range(len(zones)):
                        curr = zones[z]
                        zones[z] = (curr[0] + 1, curr[1])

                elif curr_push == "<" and zones[-1][0] > 0:
                    for z in range(len(zones)):
                        curr = zones[z]
                        zones[z] = (curr[0] - 1, curr[1])

                if zones[0][1] > 0:
                    for z in range(len(zones)):
                        curr = zones[z]
                        zones[z] = (curr[0], curr[1] - 1)

                    y = zones[0][1]
                    x = zones[0][0]

                else:
                    _max = 0

                    for zone in zones:
                        coor["@"].add(zone)

                        if zone[1] >= _max:
                            _max = zone[1]

                    y += 1
                    x = 2
                    print(x, y)
                    break
            print(coor["@"])
        if curr_rock == "plus":

            while True:
                zones = [
                    (x + 1, y),
                    (x, y + 1),
                    (x + 1, y + 1),
                    (x + 2, y + 1),
                    (x + 1, y + 2),
                ]

                push = push % push_length
                curr_push = push_order[push]
                push += 1

                if curr_push == ">" and zones[-1][0] < 6:
                    for z in range(len(zones)):
                        curr = zones[z]
                        zones[z] = (curr[0] + 1, curr[1])

                elif curr_push == "<" and zones[-1][0] > 0:
                    for z in range(len(zones)):
                        curr = zones[z]
                        zones[z] = (curr[0] - 1, curr[1])

                any_rock_not_taken = True

                for z in range(len(zones)):
                    curr = zones[z]
                    to_check = (curr[0], curr[1] - 1)

                    print(to_check, coor["@"])

                    if to_check in coor["@"]:
                        any_rock_not_taken = False
                        break

                if zones[0][1] > 0 and any_rock_not_taken == True:
                    for z in range(len(zones)):
                        curr = zones[z]
                        zones[z] = (curr[0], curr[1] - 1)

                    y = zones[1][1]
                    x = zones[1][0]

                else:
                    for zone in zones:
                        coor["@"].add(zone)
                    break

            print(coor["@"])


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
