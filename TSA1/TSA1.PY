
input_string = "Hello World! 123"  # Input string for character counting
# Define vowels
vowels = "aeiouAEIOU"

# Initialize counters
num_vowels = 0
num_consonants = 0
num_spaces = 0
num_others = 0

# Loop through each character in the input string
for char in input_string:
    if char.isalpha():  # Check if the character is a letter
        if char in vowels:  # Check if it's a vowel
            num_vowels += 1
        else:  # It's a consonant
            num_consonants += 1
    elif char.isspace():  # Check if it's a space
        num_spaces += 1
    else:  # It's some other character (like punctuation or numbers)
        num_others += 1

# Print the results for character counting
print("Part 1: Character Counting")
print("Vowels:", num_vowels)
print("Consonants:", num_consonants)
print("Spaces:", num_spaces)
print("Other characters:", num_others)
print()  # Print a blank line for separation

# Part 2: Sum the Digits from an Input String
input_string = "abc123def456"  # Input string for digit summing

# Initialize the sum to 0
total_sum = 0

# Loop through each character in the input string
for char in input_string:
    if char.isdigit():  # Check if the character is a digit
        total_sum += int(char)  # Convert to integer and add to total_sum

# Print the result for digit summing
print("Part 2: Sum of Digits")
print("Sum of digits:", total_sum)
print()  # Print a blank line for separation

# a. Using Nested For Statement
n = 5  # Number of rows for the first pattern
print("Part 3a: Pattern with Nested For Loops")
for i in range(1, n + 1):
    # Print leading spaces
    for j in range(n - i):
        print(" ", end="")  # Print space without a new line
    # Print numbers
    for j in range(1, i + 1):
        print(j, end="")  # Print numbers without a new line
    print()  # Move to the next line after each row

# b. Using Nested While Statement
n = 7  # Number of rows for the second pattern
print("Part 3b: Pattern with Nested While Loops")
i = 1  # Start with the first row
while i <= n:  # Loop for each row
    j = 1  # Start with the first character in the row
    while j <= i * 2 - 1:  # Print odd number of characters
        print(i, end="")  # Print the current row number
        j += 1  # Move to the next character
    print()  # Move to the next line after each row
    i += 1  # Move to the next row