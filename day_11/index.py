# import required module
import sys
# append the path of the sibling directory
sys.path.append('..')
from utils.get_input import get_sample


def find_flashes(input, y, x, counter):

  input[y][x] = 0
  counter+=1
  if y == 0:
    print(y,x)
    
  if  y < len(input)-1 and x < len(input[y])-1:
    # ------- top threee -------
    if input[y-1][x] == 9:
      find_flashes(input, y-1, x, counter)
    else:
      input[y-1][x]+=1

    if input[y-1][x-1] == 9:
      find_flashes(input, y-1, x-1, counter)
    else:
      input[y-1][x-1]+=1

    if input[y-1][x+1] == 9:
      find_flashes(input, y-1, x+1, counter)
    else:
      input[y-1][x+1]+=1
  #   --------left and right side numbers---------
    if input[y][x-1] == 9:
      find_flashes(input, y, x-1, counter)
    else:
      input[y][x-1]+=1

    if input[y][x+1] == 9:
      find_flashes(input, y, x+1, counter)
    else:
      input[y][x+1]+=1

    # ------- bottom threee -------
    if input[y+1][x] == 9:
      find_flashes(input, y+1, x, counter)
    else:
      input[y+1][x]+=1

    if input[y+1][x-1] == 9:
      find_flashes(input, y+1, x-1, counter)
    else:
      input[y+1][x-1]+=1

    if input[y+1][x+1] == 9:
      find_flashes(input, y+1, x+1, counter)
    else:
      input[y+1][x+1]+=1

  if y == len(input)-1 and x ==len(input[y])-1:
     if input[y-1][x] == 9:
      find_flashes(input, y-1, x, counter)
     else:
      input[y-1][x]+=1

     if input[y-1][x-1] == 9:
        find_flashes(input, y-1, x-1, counter)
     else:
        input[y-1][x-1]+=1

     if input[y][x-1] == 9:
      find_flashes(input, y, x-1, counter)
     else:
      input[y][x-1]+=1
     
    

  return counter

def find_flash_count(input):
  sum = 0
  for x in range(len(input)):
    input[x] =  list(input[x])
    for j in range(len(input[x])):
      input[x][j] = int(input[x][j])


  for i in range(1,10):
    for m in range(10):
      for n in range(10):
        
        if input[m][n] == 9:
         sum+=find_flashes(input, m, n, 0)
        
        input[m][n] = input[m][n]+1


    print("-----------")
    for y in input:
      print(y, i)

  # for y in input:
  #   print(y)
  return sum


print(find_flash_count(get_sample("sample_input.txt")))