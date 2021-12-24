# import required module
import sys
import math
# append the path of the sibling directory
sys.path.append('..')
from utils.get_input import get_sample_seperator

def decrement_array_int(starting_set):
  starting_set.reverse()

  string_ints = [str(int) for int in starting_set]
  string_int = "".join(string_ints)

  for x in range(len(string_int)):
    if string_int[x] == "0":
      value = int("".join(string_ints)) - 1
    else:
      value = int("".join(string_ints)) - 1
    
  s = str(value)
  temp = []

  for y in range(1, len(s)+1):
    temp.append(int(s[len(s)-y]))

  return temp

def custom_ALU(commands, variables, input_number):

  for instruction in commands:
    params = instruction.split(" ") # split the line into 3 values -> ["eql", "x", y]
    command = params[0]
    value_1 = variables[params[1]]

    if len(params) > 2:
      if params[2] in ['x','y', 'z', 'w']:
        value_2 = variables[params[2]]
      else:
        value_2 = int(params[2])
    else:
      value_2 = 0
    
    # params[0], command can be one of 6 values, consider each value and 
    # make that operation and store the value in params[1]
    if command == "inp":
      variables[params[1]] = input_number
    elif command == "add":
      variables[params[1]] = value_1 + value_2
    elif command == "mul":
      variables[params[1]] = value_1 * value_2
    elif command == "div":
      variables[params[1]] = math.floor(value_1 / value_2)
    elif command == "mod":
      variables[params[1]] = value_1 % value_2
    elif command == "eql":
      variables[params[1]] = 1 if value_1 == value_2 else 0

  return variables


def check_variable_inputs():
  total = []
  starting_set = [9,9,9,9,9,9,9]
  current_index = 0



  standard_input = get_sample_seperator("input.txt","\n")
  # print(standard_input[0:18])
  # print(standard_input[18:36])
  # print(standard_input[36:54])

  zero_in_z = False
  while zero_in_z == False:
    temp = []
    current_index = 0
    starting_set = decrement_array_int(starting_set)
    print(starting_set)
    variables = {
    "x": 0,
    "y": 0,
    "z": 0,
    "w": 0
    }
    for i in range(14):
      if (i+1) in [1,2,3,4,6,7,12]:
        item = starting_set[current_index]
        current_index+=1
        temp.append(item)
        variables = custom_ALU(standard_input[i*18:(i+1)*18], variables, item)

      elif (i+1) in [5,8,9,10,11,13,14]:
        c = math.floor(variables["z"]%26)
        if c > 0 and c<=9:
          temp.append(c)
          variables = custom_ALU(standard_input[i*18:(i+1)*18], variables, c)

      if variables["z"] == 0:
        return temp
      
    # print(temp)
    total.append(temp)
  
  print(variables)

check_variable_inputs()