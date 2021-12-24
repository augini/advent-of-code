def decrement_array_int(starting_set):
  starting_set.reverse()

  string_ints = [str(int) for int in starting_set]
  string_int = "".join(string_ints)

  for x in range(len(string_int)):
    if string_int[x] == "1":
      value = int("".join(string_ints)) - 2
    else:
      value = int("".join(string_ints)) - 1
    
  print(value)
  s = str(value)

  temp = []

  for y in range(1, len(s)+1):
    temp.append(int(s[len(s)-y]))

  return temp

starting_set = [0, 1, 9, 5, 9, 9, 9]

print(decrement_array_int(starting_set))