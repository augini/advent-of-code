# import required module
import sys
# append the path of the sibling directory
sys.path.append("..")
from utils.get_input import get_sample


# part_1
def find_power_consumption(input):
  gamma_rate=epsilon_rate=''
  zero_count=one_count=0

  for y in range(len(input[0])):
    for x in range(len(input)):
      if input[x][y]=='0':
        zero_count+=1
      else:
        one_count+=1

    if zero_count > one_count:
       gamma_rate+="0"
       epsilon_rate+="1"
    else:
       gamma_rate+="1"
       epsilon_rate+="0"

    zero_count=one_count=0

  return int(gamma_rate,2) * int(epsilon_rate,2)

# print(find_power_consumption(get_sample("sample_input.txt"))) 


#part_2
def part_2(input):
  o_rating = calculate_rating(input,"1","0")
  sc_rating = calculate_rating(input,"0","1")

  return int(o_rating[0],2) * int(sc_rating[0],2)

# helper function to calculate rating
def calculate_rating(input, filter_one, filter_two):
  zero_count=one_count=0

  for y in range(len(input[0])):
    for x in range(len(input)):
      if input[x][y]=='0':
        zero_count+=1
      else:
        one_count+=1

    if one_count >= zero_count:
      filter_input = filter(lambda report: report[y] == filter_one, input)
      input = list(filter_input)

    elif zero_count > one_count:
      filter_input = filter(lambda report: report[y] == filter_two, input)
      input = list(filter_input)
    zero_count=one_count=0

    if len(input) == 1:
      return input

  return input


print(part_2(get_sample("sample_input.txt"))) 