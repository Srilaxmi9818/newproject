def divide_numbers():
    try:
        # Get inputs from the user
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        
        # Perform division
        result = numerator / denominator
        
        # Print the result
        print("Result of division:", result)
        
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Please enter valid numeric inputs.")

# Example usage
divide_numbers()
