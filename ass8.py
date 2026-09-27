# Experiment No. 8
# File Handling and I/O - Reading and Writing Files

# Open the input file in read mode
file = open("input.txt", "r")

# Read all lines from the file
lines = file.readlines()

# Count the number of lines
total_lines = len(lines)

# Extract the first two lines
first_two_lines = lines[:2]

# Close the input file
file.close()

# Display the total number of lines
print("Total number of lines:", total_lines)

print("\nFirst two lines:")
for line in first_two_lines:
    print(line.strip())

# Open the output file in write mode
output_file = open("output.txt", "w")

# Write the first two lines into the output file
output_file.writelines(first_two_lines)

# Close the output file
output_file.close()

print("\nFirst two lines have been written to output.txt")
