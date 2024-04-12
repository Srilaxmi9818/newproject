while True:
    try:
        user_input = input("Enter data to append to file (type 'EXIT' to quit): ")
        if user_input.upper() == 'EXIT':
            break
        with open("user_data.txt", "a") as file:
            file.write(user_input + "\n")
    except IOError:
        print("Error: Could not write to file.")
    except Exception as e:
        print("An unexpected error occurred:", e)
    else:
        print("Data appended successfully.")

print("Program terminated.")
