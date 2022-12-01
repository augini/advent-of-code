from pathlib import Path
from itertools import product
from collections import defaultdict

def parse(filename):
    INPUTS_FILE = Path(__file__).parent / filename
    with open(INPUTS_FILE) as f:
        input_string = f.read()
    return input_string.split("\n")


def reboot_reactor(input):
  reactor_cubes = {}

  # convert 
  # on x=-20..26,y=-36..17,z=-47..7 
  #'on', -20, 26, -36, 17, -47, 7]
  
  for i in range(0, len(input)):
    dimensions = input[i].split(",")
    [switch, x_range] = dimensions[0].split(" ")

     # get x range
    [x_min, x_max] = x_range.split("..")
    x_min = x_min.replace("x=","")

    # get y range
    [y_min, y_max] = dimensions[1].split("..")
    y_min = y_min.replace("y=","")

    # get z range
    [z_min, z_max] = dimensions[2].split("..")
    z_min = z_min.replace("z=","")
    input[i] = [switch, int(x_min), int(x_max), int(y_min), int(y_max), int(z_min), int(z_max)]


  # start toggling the cubes
  for ins in input:
    if ins[1] < -50 or ins[2] > 50 or ins[3] < -50 or ins[4]> 50 or ins[5] < -50 or ins[6] >50: 
      continue
    
    for x in range(ins[1],ins[2]+1):
      for y in range(ins[3],ins[4]+1):
        for z in range(ins[5],ins[6]+1):

          if ins[0] == "on":
            reactor_cubes[f"{x,y,z}"] = 1
          else:
            reactor_cubes[f"{x,y,z}"] = 0

  filtered = filter(lambda on: on == 1, list(reactor_cubes.values()))

  return len(list(filtered))


print("part 1: ", reboot_reactor(parse(filename="input.txt")))


# for x, y, z in product(range(0, 1000), range(0, 1000), range(0, 1000)):
#   m = f"{x,y,z}"

with open("./input.txt") as fin:
    raw_data = fin.read().strip().split("\n")
steps = []

def volume(bounds):
    # Compute volume of cuboid
    p = 1
    for b in bounds:
        assert b[1] >= b[0]
        p *= abs(b[1] - b[0]) + 1
    return p


def overlap(bounds1, bounds2):
    # Intersect two cubes to find a new cube!
    ans = []
    for b1, b2 in zip(bounds1, bounds2):
        if b1[1] < b2[0] or b2[1] < b1[0]:
            return None

        bounds = (max(b1[0], b2[0]), min(b1[1], b2[1]))
        ans.append(bounds)

    return tuple(ans)


for line in raw_data:
    parts = line.split(" ")
    switch = parts[0] == "on"
    bounds = []
    for axis in parts[1].split(","):
        axis = axis.split("..")
        bounds.append((int(axis[0][2:]), int(axis[1])))

    steps.append((switch, tuple(bounds)))


counts = defaultdict(int)
for i in range(len(steps)):
    switch, bounds = steps[i]

    new_counts = defaultdict(int)
    keys = set(counts.keys())
    for o_cube in keys:
        o_switch = counts[o_cube] > 0
        o = overlap(bounds, o_cube)
        if o == None:
            continue

        new_counts[o] -= counts[o_cube]  # Reset to 0

    if switch:
        new_counts[bounds] += 1

    for c in new_counts:
        counts[c] += new_counts[c]


ans = 0
for cube in counts:
    ans += volume(cube) * counts[cube]
    
print("part 2: ", ans)