# Open the file numbers.txt in read mode
file = open("numbers.txt", "r")

# Read each line from the file
for line in file:
    # Remove whitespace and split numbers by comma
    numbers = line.strip().split(",")
    # Convert string numbers to integers
    numbers = list(map(int, numbers))
    # Compute the sum of the numbers
    total = sum(numbers)
    # Convert sum to string and check if it's a palindrome
    if str(total) == str(total)[::-1]:
        result = "Palindrome"
    else:
        result = "Not a palindrome"
    # Print the result
    print(f"Line: {line.strip()} (sum {total}) - {result}")

# Close the file after reading
file.close()
