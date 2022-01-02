from collections import Counter, defaultdict
import copy

def get_values(dictionary):
  points = list(dictionary.keys())[0]
  path = list(dictionary.values())[0]

  return points, path

def lowest_risk_level_path(path):
  new_path = [] # array of integer arrays

  # convert string into array of integer arrays
  path = path.split("\n")
  for line in range(len(path)):
    temp = []
    for char in path[line]:
      temp.append(int(char))

    new_path.append(temp)
  
  # start traversing using BFS
  _queue = [{"0,0":[]}]

  # steps and sum of the steps, in conclusion weight of the path
  pairs = {}

  all_paths = []

  while len(_queue) > 0:
    point, path = get_values(_queue.pop(0))
    [x, y] = point.split(",")
    x = int(x)
    y = int(y)


    # ---------------------------------
    path_1 =copy.deepcopy(path)
    path_2 =copy.deepcopy(path)

    # ---------------------------------
    if x+1 < len(new_path[0]):
      path_1.append(new_path[x+1][y])

      current_sum = sum(path_1)
      current_path_length = len(path_1)

      # ---------------------------------- #
      if current_path_length not in pairs:
        pairs[current_path_length] = current_sum
      else:
        if current_sum < pairs[current_path_length]:
          pairs[current_path_length] = current_sum
        
      # ---------------------------------- #
      
      if pairs[current_path_length] >= current_sum:
        _queue.append({f"{x+1},{y}":path_1})

    if y+1 < len(new_path):
      path_2.append(new_path[x][y+1])

      current_sum = sum(path_2)
      current_path_length = len(path_2)
      
      # ---------------------------------- #
      if current_path_length not in pairs:
        pairs[current_path_length] = current_sum
      else:
        if current_sum < pairs[current_path_length]:
          pairs[current_path_length] = current_sum
      # ---------------------------------- #
      
      if pairs[current_path_length] >= current_sum:
        _queue.append({f"{x},{y+1}":path_2})

    if (x+1 < len(new_path[0])) == False and (y+1 < len(new_path)) == False:
      print(path)
      all_paths.append(sum(path))
      continue

  return min(all_paths)

print(lowest_risk_level_path("""1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""))