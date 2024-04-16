def count_unique_alphabetic_chars(input_string):
    # Convert the string to lowercase and filter out non-alphabetic characters
    filtered_string = ''.join(char.lower() for char in input_string if char.isalpha())
    
    # Convert the filtered string to a set to automatically remove duplicates
    unique_chars_set = set(filtered_string)
    
    # Return the number of unique alphabetic characters
    return len(unique_chars_set)

# Example usage
input_str = "Hello, World! This is a test string."
print("Number of unique alphabetic characters:", count_unique_alphabetic_chars(input_str))
