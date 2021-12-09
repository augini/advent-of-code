# import required module
import sys
# append the path of the sibling directory
sys.path.append('..')
from utils.get_input import get_sample

# part 1
def find_low_points(input):
  low_points = []

  for x in range(len(input)):
    for y in range(len(input[x])):
      if (y < len(input[x])-1 and y > 0 and input[x][y] < input[x][y-1] and input[x][y] < input[x][y+1]) or (y == len(input[x])-1 and input[x][y] < input[x][y-1]) or (y == 0 and input[x][y] < input[x][y+1]):
        if (x==0 and input[x][y] < input[x+1][y]) or (x==len(input)-1 and input[x][y] < input[x-1][y]):
          low_points.append(input[x][y])
        elif x !=len(input)-1 and input[x][y] < input[x+1][y] and input[x][y] < input[x-1][y]:
          low_points.append(input[x][y])

  sum =0 
  print(low_points)
  for i in low_points:
    sum+=int(i)+1
  return sum


# print(find_low_points(get_sample("input.txt")))

def calculate_paths(input, x, y, basin, indexes):
  # print(x,y)
  if int(input[x][y-1]) - int(input[x][y]) in (0,1,2) and int(input[x][y-1]) != 9:
    if f"{x,y-1}" not in indexes:
      basin.append(input[x][y-1])
      indexes.append(f"{x,y-1}")
      calculate_paths(input, x, y-1, basin, indexes)
      
  if y < len(input[x])-1 and int(input[x][y+1]) - int(input[x][y]) in (0,1,2) and int(input[x][y+1]) != 9 :
    if f"{x,y+1}" not in indexes:
      basin.append(input[x][y+1])
      indexes.append(f"{x,y+1}")
      calculate_paths(input, x, y+1, basin, indexes)

  if x == 0 and int(input[x+1][y]) - int(input[x][y]) in (0,1,2) and int(input[x+1][y]) != 9:
    if f"{x+1,y}" not in indexes:
      basin.append(input[x+1][y])
      indexes.append(f"{x+1,y}")
      calculate_paths(input, x+1, y, basin, indexes)

  if x == len(input)-1 and int(input[x-1][y]) - int(input[x][y]) in (0,1,2) and int(input[x-1][y]) != 9:
    if f"{x-1,y}" not in indexes:
      basin.append(input[x-1][y])
      indexes.append(f"{x-1,y}")
      calculate_paths(input, x-1, y, basin, indexes)
  
  if x > 0 and x < len(input)-1 and int(input[x+1][y]) - int(input[x][y]) in (0,1,2) and int(input[x+1][y]) != 9:
    if f"{x+1,y}" not in indexes:
      basin.append(input[x+1][y])
      indexes.append(f"{x+1,y}")
      calculate_paths(input, x+1, y, basin, indexes)

  if x > 0 and x < len(input)-1 and int(input[x-1][y]) - int(input[x][y]) in (0,1,2) and int(input[x-1][y]) != 9:
    if f"{x-1,y}" not in indexes:
      basin.append(input[x-1][y])
      indexes.append(f"{x-1,y}")
      calculate_paths(input, x-1, y, basin, indexes)
  
  return len(basin)+1
  

# part 2
def find_basins(input):
  low_points = []
  sizes = []

  for x in range(0,len(input)):
    for y in range(len(input[x])):
      if (y < len(input[x])-1 and y > 0 and input[x][y] < input[x][y-1] and input[x][y] < input[x][y+1]) or (y == len(input[x])-1 and input[x][y] < input[x][y-1]) or (y == 0 and input[x][y] < input[x][y+1]):
        if (x==0 and input[x][y] < input[x+1][y]) or (x==len(input)-1 and input[x][y] < input[x-1][y]):
          low_points.append(input[x][y])
          sizes.append(calculate_paths(input, x, y, [],[]))

        elif x !=len(input)-1 and input[x][y] < input[x+1][y] and input[x][y] < input[x-1][y]:
          low_points.append(input[x][y])
          sizes.append(calculate_paths(input, x, y, [],[]))

  sizes.sort()

  result = 1
  max_three = sizes[len(sizes)-3:]

  for x in max_three:
    result *= x
  return result

print(find_basins(get_sample("input.txt")))