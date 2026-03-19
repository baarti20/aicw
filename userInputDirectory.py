import os  # Module for interacting with the operating system

# Prompt the user to enter a directory name
folder_name = input("Enter the name of the directory: ")

# Check if the directory already exists
if not os.path.exists(folder_name):
    os.mkdir(folder_name)  # Create the directory if it doesn't exist
    print(f"Directory '{folder_name}' created successfully!")
else:
    print(f"Directory '{folder_name}' already exists.")  # Notify if it already exists
