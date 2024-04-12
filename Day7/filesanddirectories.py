import os

def list_files_and_subdirectories(directory="."):
    try:
        print(f"Contents of directory '{directory}':")
        for root, dirs, files in os.walk(directory):
            for file in files:
                print(os.path.join(root, file))
            for dir in dirs:
                print(os.path.join(root, dir))
    except Exception as e:
        print("An unexpected error occurred:", e)

# Example usage:
directory_path = input("Enter directory path (leave blank for current directory): ").strip()
if directory_path:
    list_files_and_subdirectories(directory_path)
else:
    list_files_and_subdirectories()
