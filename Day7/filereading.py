try:
    file_name = "data.txt"
    with open(file_name, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_chars = sum(len(line) for line in lines)

    print("Number of lines:", num_lines)
    print("Number of words:", num_words)
    print("Number of characters:", num_chars)

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except PermissionError:
    print(f"Error: Permission denied to open '{file_name}'.")
except Exception as e:
    print("An unexpected error occurred:", e)
