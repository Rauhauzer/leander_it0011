def divide(a, b):
    #Returns the division of a by b, or None if b is zero.
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return a / b

def exponentiate(base, exponent):
    #Returns base raised to the power of exponent.
    return base ** exponent

def remainder(a, b):
    #Returns the remainder of a divided by b, or None if b is zero.
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return a % b

def summation(start, end):
    #Returns the summation from start to end (inclusive), or None if end < start.
    if end < start:
        print("Error: The second number must be greater than the first number.")
        return None
    return sum(range(start, end + 1))

def main():
    while True:
        print("\nMenu:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[X] - Exit")
        choice = input("Enter your choice: ").upper()

        if choice == "D":
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number (denominator): "))
            result = divide(a, b)
        elif choice == "E":
            base = float(input("Enter the base number: "))
            exponent = float(input("Enter the exponent: "))
            result = exponentiate(base, exponent)
        elif choice == "R":
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number (denominator): "))
            result = remainder(a, b)
        elif choice == "F":
            start = int(input("Enter the first number: "))
            end = int(input("Enter the second number (must be greater than first): "))
            result = summation(start, end)
        elif choice == "X":
            break
        else:
            print("Invalid choice. Try again.")
            continue

        if result is not None:
            print("Result:", result)

if __name__ == "__main__":
    main()
