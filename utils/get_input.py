

# function to convert text into list of strings
def get_sample(_dirname):
  input  = open(_dirname, "r")
  return list(input.read().split(','))

# function to read entire file content
def get_file_content(_dirname):
  input  = open(_dirname, "r")
  return input.read().split()