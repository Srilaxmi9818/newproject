import os

try:
    # Check if the directory "backup" already exists
    if os.path.exists("backup"):
        # If it exists, rename it to "backup_old"
        os.rename("backup", "backup_old")
        print("Existing 'backup' directory renamed to 'backup_old'.")
    
    # Create a new directory named "backup"
    os.mkdir("backup")
    print("New 'backup' directory created.")

except FileExistsError:
    print("Error: Directory 'backup' already exists.")
except PermissionError:
    print("Error: Permission denied to create or rename directories.")
except Exception as e:
    print("An unexpected error occurred:", e)
