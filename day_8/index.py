# import required module
import sys
# append the path of the sibling directory
sys.path.append('..')
from utils.get_input import get_sample_seperator

def count_instances(input):
  second_half = []
  for x in input:
    second_half.append(x[x.index('|')+2:len(x)])
  
  counter = 0
  for i in " ".join(second_half).split(" "):
    if len(i) in (2,4,3,7):
      counter += 1

  return counter

# print(count_instances(get_sample_seperator("input.txt", "\n")))

def decode_digits(input):
  first_half = []
  second_half = []
  decoded_outputs = []

  for x in input:
    first_half.append(x[0:x.index('|')-1])

  for x in range(len(first_half)):
    first_half[x] = first_half[x].split(" ")

  for x in input:
    second_half.append(x[x.index('|')+2:len(x)])
  for x in range(len(second_half)):
    second_half[x] = second_half[x].split(" ")

  for values in first_half:
    temp = []
    for i in values:
      if len(i) == 2:
        temp.append({"1":i})
      elif len(i) == 4:
        temp.append({"4":i})
      elif len(i) == 3:
        temp.append({"7":i})
      elif len(i) == 7:
        temp.append({"8":i})
      elif len(i) == 5:
        temp.append({"5":i})
      elif len(i) == 6:
        temp.append({"6":i})

    decoded_outputs.append(temp)
    for m in decoded_outputs:
      seven_segments = [x for x in m if x.get("7") != None][0].get("7")
      four_segments = [x for x in m if x.get("4") != None][0].get("4")

      for n in range(len(m)):
        if m[n].get("6") != None:
          old_value = m[n].get("6")

          counter = 0
          for i in old_value:
            if i not in seven_segments+four_segments:
              counter += 1
              
          # we got "9"
          if counter == 1:
             m[n] = {"9":old_value}
          elif counter == 2:
            length = len("".join(set(old_value+seven_segments)))
            if length == 7:
              # we got "6"
              m[n] = {"6":old_value}
            elif length == 6:
              # we got "0"
              m[n] = {"0":old_value}

        if m[n].get("5") != None:
          old_value = m[n].get("5")

          length = len("".join(set(old_value+four_segments)))
          if length == 7:
              # we got "2"
              m[n] = {"2":old_value}
          elif length == 6:
             length =len("".join(set(old_value+seven_segments)))
             if length == 6:
              # we got "5"
              m[n] = {"5":old_value}
             elif length == 5:
              # we got 3
              m[n] = {"3":old_value}

  total_sum = 0
  decimal = ""
  
  for x in range(len(second_half)):
    for y in second_half[x]:
      for m in range(len(decoded_outputs[x])):
        for key, value in decoded_outputs[x][m].items():
          if len(y) == len(value):
            counter=0
            for i in range(len(y)):
              if y[i] in value:
                counter += 1
            if counter == len(y):
              decimal += key

    # print(second_half[x],decimal)
    total_sum+=int(decimal)
    decimal = ""

  return total_sum

print(decode_digits(get_sample_seperator("input.txt", "\n")))
