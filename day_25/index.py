# import required module
import sys
# append the path of the sibling directory
sys.path.append('..')
from utils.get_input import get_sample


def move_sea_cucumbers(map):
  new_map = []

  for num in range(len(map)):
    temp = []
    for char in range(len(map[num])):
      temp.append(map[num][char])
    new_map.append(temp)

  has_moved = True
  counter = 0
  while has_moved:
    # move east going cucumbers first
    has_moved = False
    currently_moved = []
    for y in range(len(new_map)):
      for x in range(len(new_map[0])):
        if new_map[y][x] == ">":
          if x < len(new_map[0])-1:
            if new_map[y][x+1] == "." and f"{y,x}" not in currently_moved and f"{y,x+1}" not in currently_moved:
              new_map[y][x+1] = ">"
              new_map[y][x] = "."
              currently_moved.append(f"{y,x}")
              currently_moved.append(f"{y,x+1}")
              has_moved = True

          elif x == len(new_map[0])-1 and f"{y,x}" not in currently_moved and f"{y,0}" not in currently_moved:
            if new_map[y][0] == ".":
              new_map[y][0] = ">"
              new_map[y][x] = "."
              has_moved = True

    # move south going cucumbers next
    currently_moved = []
    for y in range(len(new_map)):
      for x in range(len(new_map[0])):
        if new_map[y][x] == "v" :

          if y < len(new_map)-1:
            if new_map[y+1][x] == "." and f"{y,x}" not in currently_moved and f"{y+1,x}" not in currently_moved:
              new_map[y+1][x] = "v"
              new_map[y][x] = "."
              currently_moved.append(f"{y,x}")
              currently_moved.append(f"{y+1,x}")
              has_moved = True

          elif y == len(new_map)-1 and f"{y,x}" not in currently_moved and f"{0,x}" not in currently_moved:
            if new_map[0][x] == ".":
              new_map[0][x] = "v"
              new_map[y][x] = "."
              has_moved = True
    counter+=1
    # print(counter)
    # for line in new_map:
    #   print("".join(line)) 
   
  # for line in new_map:
  #   print("".join(line))            
                   
  return counter


print(move_sea_cucumbers(get_sample("input.txt")))

