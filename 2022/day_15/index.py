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


def part1(data, y):
    """Solve part 1."""

    area = set()
    beacon_areas = set()

    # get the sensor and beacon coors
    for item in data:
        parts = item.split(":")
        one, two = parts[0].split(" "), parts[1].split(" ")

        x1 = int(one[-2].split("=")[-1].replace(",", ""))
        y1 = int(one[-1].split("=")[-1])

        x2 = int(two[-2].split("=")[-1].replace(",", ""))
        y2 = int(two[-1].split("=")[-1])

        sensor = (x1, y1)
        beacon = (x2, y2)
        distance = abs(x2 - x1) + abs(y2 - y1)
        beacon_areas.add(beacon)

        height = sensor[1] + distance
        if abs(y - sensor[1]) <= height:
            if (height) - y >= 0:
                diff = abs(y - sensor[1])

                left = sensor[0] - (distance - diff)
                right = sensor[0] + (distance - diff)
                for x in range(left, right + 1):
                    area.add((x, y))

    return len(area - beacon_areas)


SCANS = []
beacon_areas = set()
LIMIT = 4000000

# function to check if the point is in the given amount of Manhatten distance from the sensor
def isContained(point):
    l = len(SCANS)

    if point in beacon_areas:
        return False

    if not (0 <= point[0] <= LIMIT and 0 <= point[1] <= LIMIT):
        return False

    not_contained = 0

    for scan in SCANS:
        sensor, distance = scan

        point_distance = abs(sensor[0] - point[0]) + abs(sensor[1] - point[1])
        if point_distance > distance:
            not_contained += 1

    if not_contained == l:
        print(point[0] * 4000000 + point[1])
        print(point)

    return not_contained == l


def part2(data):
    """Solve part 2."""
    # get the sensor and beacon coors
    for item in data:
        parts = item.split(":")
        one, two = parts[0].split(" "), parts[1].split(" ")

        x1 = int(one[-2].split("=")[-1].replace(",", ""))
        y1 = int(one[-1].split("=")[-1])

        x2 = int(two[-2].split("=")[-1].replace(",", ""))
        y2 = int(two[-1].split("=")[-1])

        sensor = (x1, y1)
        beacon = (x2, y2)
        beacon_areas.add(beacon)
        distance = abs(x2 - x1) + abs(y2 - y1)

        SCANS.append((sensor, distance))

    # get the sensor and beacon coors
    for scan in SCANS:
        sensor, distance = scan
        distance += 1

        for i in range(distance):
            diff = distance - i

            l_edge_up = (sensor[0] - diff, sensor[1] + i)
            r_edge_up = (sensor[0] + diff, sensor[1] + i)

            l_edge_down = (sensor[0] - diff, sensor[1] - i)
            r_edge_down = (sensor[0] + diff, sensor[1] - i)

            if (
                isContained(l_edge_up)
                or isContained(r_edge_up)
                or isContained(l_edge_down)
                or isContained(r_edge_down)
            ):
                return (l_edge_up, r_edge_up, l_edge_down, r_edge_down)
    return 1


def solve(puzzle_input):
    # Solve the puzzle for the given input.
    # parse the given input
    data = parse(puzzle_input, 2)

    # get the solutions for each problem
    # solution1 = part1(data, 2000000)
    solution2 = part2(data)

    return 1, solution2


if __name__ == "__main__":
    #  print(sys.argv)
    for path in sys.argv[1:]:
        #   print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
