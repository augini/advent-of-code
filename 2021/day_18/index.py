# import required module
from curses.ascii import isdigit
from pathlib import Path
import math

def parse(filename):
    INPUTS_FILE = Path(__file__).parent / filename
    with open(INPUTS_FILE) as f:
        input_string = f.read()
    return input_string

# function used to explode the given pair of numbers
def explode(number):
  array = []

  # convert string into array of chars
  for i in range(len(number)):
    array.append(number[i])

  # loop througt the array and find pairs four brackets deep
  bracket_depth = 0
  new_array = []

  for i in range(len(array)):
    if bracket_depth == 4 and not isdigit(array[i]) and array[i] != ",":

       left_digit = array[i+1]
       right_digit = array[i+3]
      #  print(i,array[i])
       new_array = array[0:i]+["0"]+array[i+5:]

      #  print("".join(new_array))
      #  print(left_digit, right_digit)

      # increment leftmost number
       for x in range(i-1, 0, -1):
        if isdigit(new_array[x]):
          new_array[x] = str(int(left_digit) + int(new_array[x]))
          break

       # increment rightmost number
       for x in range(i+1, len(new_array)):
        if isdigit(new_array[x]):
          new_array[x] = str(int(right_digit) + int(new_array[x]))
          break

      #  break outer loop
       break
    if array[i] == "[":
      bracket_depth+=1
    elif array[i] == "]":
      bracket_depth-=1
  return "".join(new_array)

def split(sn_number):
  array = []

  # convert string into array of chars
  for i in range(len(sn_number)):
    if isdigit(sn_number[i]) and isdigit(sn_number[i+1]):
       number = f"{sn_number[i]}{sn_number[i+1]}"
       array.append(number)
       i=i+1
       continue
    array.append(sn_number[i])

  new_array = []
  for i in range(len(array)):
    if array[i] not in [']', ",","[" ] and int(array[i]) > 9:
      print(array)
      left_digit = math.floor(int(array[i])/2)
      right_digit = math.ceil(int(array[i])/2)

      print(left_digit, right_digit)
      new_array = array[0:i]+[f"{left_digit},{right_digit}"]+array[i+3:]
      break

  # print("".join(new_array))
  return "".join(new_array)


def snail_sum_numbers(input):
  result = split(input)
  print(result)
  return result

snail_sum_numbers(parse("sample_input.txt"))


# [[[[[9,8],1],2],3],4]
# [[[[0,9],2],3],4]

# [7,[6,[5,[4,[3,2]]]]]
# [7,[6,[5,[7,0]]]]
# [7,[6,[5,[7,0]]]]


# [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
# [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]