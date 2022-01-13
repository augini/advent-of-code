from pathlib import Path
from itertools import product


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


print(reboot_reactor(parse(filename="input.txt")))


# for x, y, z in product(range(0, 1000), range(0, 1000), range(0, 1000)):
#   m = f"{x,y,z}"
