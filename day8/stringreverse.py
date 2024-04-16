def reverse_string(input_string):
    stack = []
    # Push each character onto the stack
    for char in input_string:
        stack.append(char)
    
    reversed_string = ""
    # Pop each character from the stack to reverse the string
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string

# Example usage
input_str = "Hello, World!"
reversed_str = reverse_string(input_str)
print("Original string:", input_str)
print("Reversed string:", reversed_str)
