import itertools

# Get the number of inputs from the user
num_inputs = int(input("Enter the number of elements: "))

# Get user inputs
user_inputs = []
for i in range(num_inputs):
    user_input = input("Enter element {}: ".format(i+1))
    user_inputs.append(user_input)

# Get the maximum number of special characters from the user
max_special_chars = int(input("Enter the maximum number of special characters per line: "))

# Define special characters
special_chars = ['@', '-', '_', '#']

# Generate permutations
permutations = []
for r in range(1, num_inputs + 1):
    for comb in itertools.combinations(user_inputs + special_chars, r):
        for perm in itertools.permutations(comb):
            count_special_chars = sum(1 for char in perm if char in special_chars)
            if count_special_chars <= max_special_chars:
                permutations.append(perm)

# Open file in write mode
with open("password.txt", "w") as file:
    # Write permutations to file
    for permutation in permutations:
        file.write(''.join(permutation) + '\n')

    for permutation in permutations:
        joined_permutation = ''.join(permutation)
        start_index = 0

        if not joined_permutation[start_index].isalpha():
            start_index += 1

        capitalized_permutation = joined_permutation[:start_index] + joined_permutation[start_index:start_index + 3].capitalize() + joined_permutation[start_index + 3:]
        file.write(capitalized_permutation + '\n')

# Print success message
print("Permutations have been saved to password.txt file.")
