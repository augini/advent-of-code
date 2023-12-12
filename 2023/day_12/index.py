import sys

# Read the input from the command line argument
input_file = sys.argv[1]
input_data = open(input_file).read().strip()

# Split the input into lines
lines = input_data.split("\n")

# Convert the input into a 2D grid
grid = [[cell for cell in row] for row in lines]
DP = {}


# Function to calculate the number of valid configurations
def count_valid_configurations(dots, blocks, dot_index, block_index, current_length):
    # Define a key for dynamic programming memoization
    key = (dot_index, block_index, current_length)

    if key in DP:
        return DP[key]

    # Check if we have reached the end of the dots
    if dot_index == len(dots):
        # Check if we have used all the blocks and the current block length is 0
        if block_index == len(blocks) and current_length == 0:
            return 1
        elif block_index == len(blocks) - 1 and blocks[block_index] == current_length:
            return 1
        else:
            return 0

    ans = 0

    for character in [".", "#"]:
        # Check if the current dot matches the current character or is a wildcard '?'
        if dots[dot_index] == character or dots[dot_index] == "?":
            if character == "." and current_length == 0:
                ans += count_valid_configurations(
                    dots, blocks, dot_index + 1, block_index, 0
                )
            elif (
                character == "."
                and current_length > 0
                and block_index < len(blocks)
                and blocks[block_index] == current_length
            ):
                ans += count_valid_configurations(
                    dots, blocks, dot_index + 1, block_index + 1, 0
                )
            elif character == "#":
                ans += count_valid_configurations(
                    dots, blocks, dot_index + 1, block_index, current_length + 1
                )

    # Memoize the result and return
    DP[key] = ans
    return ans


for is_part2 in [False, True]:
    total_configurations = 0

    for line in lines:
        dots, blocks = line.split()

        if is_part2:
            dots = "?".join([dots, dots, dots, dots, dots])
            blocks = ",".join([blocks, blocks, blocks, blocks, blocks])

        # Convert blocks to a list of integers
        blocks = [int(x) for x in blocks.split(",")]

        DP.clear()

        configurations = count_valid_configurations(dots, blocks, 0, 0, 0)

        # Accumulate the result
        total_configurations += configurations

    # Print the result for the current part
    print(total_configurations)
