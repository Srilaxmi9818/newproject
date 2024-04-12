while True:
    try:
        user_input = input("Enter a number or type 'quit' to exit: ")
        if user_input.lower() == 'quit':
            break
        number = float(user_input)
        print("Square of", number, "is", number ** 2)
    except ValueError:
        print("Error: Please enter a valid numeric input.")
