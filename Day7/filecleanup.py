import os

def delete_files(directory, extension):
    try:
        # List all files in the directory
        files = os.listdir(directory)
        
        # Iterate through the files and delete those with the specified extension
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(directory, file)
                os.remove(file_path)
                print(f"Deleted: {file_path}")

        print("File cleanup completed.")

    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to delete files in '{directory}'.")
    except Exception as e:
        print("An unexpected error occurred:", e)

# Example usage
directory_path = input("Enter the directory path: ").strip()
file_extension = input("Enter the file extension (e.g., '.txt'): ").strip()

delete_files(directory_path, file_extension)
