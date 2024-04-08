
# Create the string
text = "Learning Python is fun!"

# Display the string on the console
print(text)



# Define the string
string = "Hello, World!"

# Find and print the length of the string
length = len(string)
print(f"\nThe length of the string {string} is {length}")




print("\nManipulating strings and characters")
# Define the string
print("\nString Slicing")
string = "Hello, Python!"
print("Current String is:",string)
# Slice the string to include only "Python"
substring = string[7:13]

# Print the sliced substring
print("Sliced string is",substring)





# Define the string
print("\nString Methods")
string = "python programming"
print("Current String is:",string)
# Convert the string to uppercase
uppercase_string = string.upper()

# Replace spaces with underscores
modified_string = uppercase_string.replace(" ", "_")

# Print the modified string
print("Modified string is",modified_string)

# Get input from the user
user_string = input("Enter a string: ")

# Convert the string to lowercase and remove spaces
user_string = user_string.lower().replace(" ", "")

# Check if the string is equal to its reverse
if user_string == user_string[::-1]:
    print("Yes, the string is a palindrome.")
else:
    print("No, the string is not a palindrome.")
