print("PRIME OR NOT")
def is_prime(number):
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    elif number == 2:
        return True   # 2 is a prime number
    else:
        # Check if the number is divisible by any integer from 2 to the square root of the number
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False  # If the number is divisible by any other number, it's not prime
        return True  # If the number is not divisible by any other number, it's prime

# Test the function
num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")


print("FACTORIAL OF A NUMBER")
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Test the function
num = int(input("Enter a number: "))
print("Factorial of", num, "is:", factorial(num))


print("Understanding def and lambda")
def greet(name):
    print("Hello,", name + "! Welcome!")

# Test the function
name = input("Enter your name: ")
greet(name)



addition = lambda x, y: x + y
# Test the lambda function
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("The sum is:", addition(num1, num2))


#Python built in functions

# Define the list
numbers = [1, 2, 3, 4, 5]

# Use the map function to square each number in the list
squared_numbers = list(map(lambda x: x ** 2, numbers))

# Print the squared numbers
print("Squared numbers:", squared_numbers)

# Use the filter function to extract squares greater than 10
filtered_squares = list(filter(lambda x: x > 10, squared_numbers))

# Print the resulting list
print("Filtered squares greater than 10:", filtered_squares)



# Define the list
fruits = ['blueberry', 'apple', 'banana']

# Sort the list in ascending order using the sorted function
sorted_fruits = sorted(fruits)

# Print the sorted list
print("Sorted list:", sorted_fruits)

