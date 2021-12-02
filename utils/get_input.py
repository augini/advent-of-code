

# function to convert text into list of strings
def get_sample(_dirname):
  input  = open(_dirname, "r")
  return list(input.read().split())