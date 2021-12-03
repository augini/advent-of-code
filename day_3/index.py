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
       gamma_rate=gamma_rate+"0"
       epsilon_rate=epsilon_rate+"1"
    else:
       gamma_rate=gamma_rate+"1"
       epsilon_rate=epsilon_rate+"0"

    zero_count=one_count=0

  return int(gamma_rate,2) * int(epsilon_rate,2)


#part_2
def part_2(input):
  zero_count=one_count=0
  oxygen_rating=scrubber_rating=input

  for y in range(0, len(oxygen_rating[0])):
    for x in range(len(oxygen_rating)):
      if oxygen_rating[x][y]=='0':
        zero_count+=1
      else:
        one_count+=1
     
    if one_count >= zero_count:
      filter_oxygen_rating = filter(lambda report: report[y] == '1', oxygen_rating)
      oxygen_rating = list(filter_oxygen_rating)

    elif zero_count > one_count:
      filter_oxygen_rating = filter(lambda report: report[y] == '0', oxygen_rating)
      oxygen_rating = list(filter_oxygen_rating)
    zero_count=one_count=0



  for y in range(0, 8):
    for x in range(len(scrubber_rating)):
      if scrubber_rating[x][y]=='0':
        zero_count+=1
      else:
        one_count+=1
    
    if one_count >= zero_count:
      filter_scrubber_rating = filter(lambda report: report[y] == '0', scrubber_rating)
      scrubber_rating = list(filter_scrubber_rating)
    elif zero_count > one_count:
      filter_scrubber_rating = filter(lambda report: report[y] == '1', scrubber_rating)
      scrubber_rating = list(filter_scrubber_rating)
    zero_count=one_count=0


  print(oxygen_rating,scrubber_rating)
  return int(oxygen_rating[0],2) * int(scrubber_rating[0],2)

print(part_2(get_sample("input.txt")))