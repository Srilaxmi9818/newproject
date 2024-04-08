# Get input from the user
principal = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest (in percentage): "))
time = float(input("Enter the time period (in years): "))

# Calculate simple interest
simple_interest = (principal * rate_of_interest * time) / 100

# Print the result
print("Simple Interest:", simple_interest)
