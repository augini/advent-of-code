import math
from pathlib import Path
from itertools import product

def parse(filename):
    INPUTS_FILE = Path(__file__).parent / filename
    with open(INPUTS_FILE) as f:
        input_string = f.read()
    return input_string.split("\n")

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
  print(s)
  temp = []

  for y in range(0, len(s)):
    temp.append(int(s[y]))
    
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


# def check_variable_inputs():
#   total = []
#   starting_set = [9,9,9,9,9,9,9]
#   current_index = 0

#   standard_input = parse("sample_input.txt")

#   print(standard_input)

increments = {"0": 12, "1": 10, "2": 8, "3": 4,"5": 10, "6": 6, "11": 6}
required =  {"4": 0, "7": 12, "8": 15, "9": 15, "10": 4, "12": 5, "13": 12}

def make_operations(digits):
    z = 0
    res = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    idx = 0

    for i in range(14):
        increment = increments[f"{i}"] if f"{i}" in increments.keys() else None
        mod_req = required[f"{i}"] if f"{i}" in required.keys() else None

        if increment == None:
            if mod_req != None:
              res[i] = ((z % 26) - mod_req)
              z = math.floor(z/26)
              if not (1 <= res[i] <= 9):
                  return False

        else:
            if increment != None:
              z = z * 26 + digits[idx] + increment
              res[i] = digits[idx]
              idx += 1

    return res

# logic tried 3 weeks ago
def check_variable_inputs():
  total = []
  starting_set = [9,9,9,9,9,9,9]
  current_index = 0

  standard_input = parse("input.txt")

  input_range = product(range(9,0,-1), repeat=7)

  # zero_in_z = False
  # while zero_in_z == False:
  #   temp = []
  #   current_index = 0
  #   starting_set = decrement_array_int(starting_set)
  #   if 0 in starting_set:
  #     continue
  #   print(starting_set)
  #   variables = {"x": 0, "y": 0, "z": 0, "w": 0 }

  #   for i in range(14):
  #     if (i+1) in [1,2,3,4,6,7,12]:
  #       item = starting_set[current_index]
  #       current_index+=1
  #       temp.append(item)
  #       variables = custom_ALU(standard_input[i*18:(i+1)*18], variables, item)

  #     elif (i+1) in [5,8,9,10,11,13,14]:
  #       c = math.floor(variables["z"]%26)
  #       if c > 0 and c<=9:
  #         temp.append(c)
  #         variables = custom_ALU(standard_input[i*18:(i+1)*18], variables, c)

  #     if variables["z"] == 0:
  #       print(variables)
  #       return temp
      
    # print(temp)
    # total.append(temp)

  for digits in input_range:
    res = make_operations(digits)
    if res:
        print("".join([str(i) for i in res]))
        break
  # print(variables)

check_variable_inputs()

