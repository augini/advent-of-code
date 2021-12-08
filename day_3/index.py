# import required module
import sys
# append the path of the sibling directory
sys.path.append("..")
from utils.get_input import get_sample


# part_1
def find_power_consumption(input):
  gamma_rate=epsilon_rate=''
  zero_count=one_count=0

  for y in range(0, len(input[0])):
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
  zero_count=one_count=0
  o_rating=sc_rating=input

  for y in range(len(o_rating[0])):
    for x in range(len(o_rating)):
      if o_rating[x][y]=='0':
        zero_count+=1
      else:
        one_count+=1

    if one_count >= zero_count:
      filter_o_rating = filter(lambda report: report[y] == '1', o_rating)
      o_rating = list(filter_o_rating)

    elif zero_count > one_count:
      filter_o_rating = filter(lambda report: report[y] == '0', o_rating)
      o_rating = list(filter_o_rating)
    zero_count=one_count=0
    if len(o_rating) == 1:
      break

  for y in range(len(sc_rating[0])):
    for x in range(len(sc_rating)):
      if sc_rating[x][y]=='0':
        zero_count+=1
      else:
        one_count+=1

    if one_count >= zero_count:
      filter_sc_rating = filter(lambda report: report[y] == '0', sc_rating)
      sc_rating = list(filter_sc_rating)
    elif zero_count > one_count:
      filter_sc_rating = filter(lambda report: report[y] == '1', sc_rating)
      sc_rating = list(filter_sc_rating)
    zero_count=one_count=0

    if len(sc_rating) == 1:
      break


  return int(o_rating[0],2) * int(sc_rating[0],2)

print(part_2(get_sample("sample_input.txt"))) 