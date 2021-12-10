# import required module
import sys
from collections import defaultdict
# append the path of the sibling directory
sys.path.append('..')
from utils.get_input import get_sample

def find_number_points(input):
  coordinates = []

  # remove -> and store the coordinates in 2d array
  for line in range(0,len(input),3):
    coordinates.append([input[line], input[line+2]])
  coor_set = defaultdict(int)

  for cor in coordinates:
        x1,x2 = int(cor[0].split(',')[0]), int(cor[1].split(',')[0])
        y1,y2 = int(cor[0].split(',')[1]), int(cor[1].split(',')[1])

        if x1 == x2:
          for y in range(min(y1, y2),  max(y1, y2)+1):
              coor_set[f"{x1},{y}"] += 1
        elif y1 == y2:
          for x in range(min(x1, x2), max(x1, x2)+1):
              coor_set[f"{x},{y1}"]+=1
  points = coor_set.values()
  result = filter(lambda x: x >= 2, points)
  return len(list(result))

# print(find_number_points(get_sample("input.txt")))

# part 2
def find_number_points(input):
  coordinates = []

  # remove -> and store the coordinates in 2d array
  for line in range(0,len(input),3):
    coordinates.append([input[line], input[line+2]])
  coor_set = defaultdict(int)

  for cor in coordinates:
        x1,x2 = int(cor[0].split(',')[0]), int(cor[1].split(',')[0])
        y1,y2 = int(cor[0].split(',')[1]), int(cor[1].split(',')[1])

        if x1 == x2:
          for y in range(min(y1, y2),  max(y1, y2)+1):
              coor_set[f"{x1},{y}"] += 1
        elif y1 == y2:
          for x in range(min(x1, x2), max(x1, x2)+1):
              coor_set[f"{x},{y1}"]+=1
        elif abs(x1 - x2) == abs(y1 - y2):
          min_x = min(x1, x2)
          max_x = max(x1, x2)

          min_y = min(y1, y2)
          max_y = max(y1, y2)

          for i in range(min_x, max_x+1):
            for j in range(min_y, max_y+1):
              if i == j:
                coor_set[f"{i},{j}"] += 1
              if i >= max_y:
                break

  points = coor_set.values()
  result = filter(lambda x: x >= 2, points)
  return len(list(result))

print(find_number_points(get_sample("input.txt")))