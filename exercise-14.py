# Print a downward Half-Pyramid Pattern of Star (asterisk)

# Number of rows
rows = 5

# Nested loop
for i in range(0, rows):
    for j in range(0, i + 1):
    # Print asterisk
        print("*", end=" ")
    # Add new lines for each row
    print()