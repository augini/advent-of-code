
# import required module
import sys
# append the path of the sibling directory
sys.path.append("..")
from utils.get_input import get_sample


# part_1
def find_position(input):
  horizontal_position = 0
  vertical_position = 0
  for x in range(0, len(input), 2):
    if input[x] == "forward":
      horizontal_position += int(input[x+1])
    elif input[x] == "up":
      vertical_position -= int(input[x+1])
    elif input[x] == "down":
      vertical_position += int(input[x+1])

  return horizontal_position*vertical_position



# print(find_position(get_sample('sample_input.txt')))
# print(find_position(get_sample('input.txt')))


# part_2
def find_aim(input):
  horizontal_position = 0
  depth = 0
  aim = 0

  for x in range(0, len(input),2):
    current = int(input[x+1])
    if input[x] == "forward":
      horizontal_position += current
      if aim != 0:
        depth += current * int(aim)
    elif input[x] == "up":
      aim -= current
    elif input[x] == "down":
      aim += current

  return horizontal_position*depth



print(find_aim(get_sample('sample_input.txt')))
