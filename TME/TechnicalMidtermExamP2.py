# List of month names in order (index 0 corresponds to January)
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

# Get the date input from the user
date = input("Enter the date (mm/dd/yyyy): ")

# Split the date input into parts: month, day, and year
parts = date.split("/")

# Convert month number to month name
month = months[int(parts[0]) - 1]  # Convert to integer and get corresponding month name

# Convert day to integer to remove leading zeros (if any)
day = int(parts[1])

# Extract the year as it is
year = parts[2]

# Print the formatted date
print(f"Date Output: {month} {day}, {year}")
