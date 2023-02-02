import os
import sys
import shutil

def display_files(directory):
    if not os.path.exists(directory):
        return f"Directory '{directory}' does not exist"
    try:
        return os.listdir(directory)
    except Exception as e:
        return f"An error occurred while accessing the directory: {e}"

def make_directory(name, path=None):
    if not name or any(char in name for char in "\\/:*?\"<>|"):
        return "Invalid directory name. Please enter a valid name without any of the following characters: \\ / : * ? \" < > |"
    
    if path:
        directory = os.path.join(path, name)
    else:
        directory = name
    try:
        os.mkdir(directory)
        return f"Directory '{directory}' created successfully"
    except Exception as e:
        return f"An error occurred while creating the directory '{directory}': {e}"

def delete_directory(directory):
    if not os.path.exists(directory):
        return f"Directory '{directory}' does not exist"
    try:
        shutil.rmtree(directory)
        return f"Directory '{directory}' deleted successfully"
    except Exception as e:
        return f"An error occurred while deleting the directory '{directory}': {e}"

def rename_directory(old_name, new_name):
    if not os.path.exists(old_name):
        return f"Directory '{old_name}' does not exist"
    if not new_name or any(char in new_name for char in "\\/:*?\"<>|"):
        return "Invalid new directory name. Please enter a valid name without any of the following characters: \\ / : * ? \" < > |"
    
    try:
        os.rename(old_name, new_name)
        return f"Directory '{old_name}' renamed to '{new_name}' successfully"
    except Exception as e:
        return f"An error occurred while renaming the directory '{old_name}': {e}"

def search_directories(name, path):
    if not os.path.exists(path):
        return f"Path '{path}' does not exist"
    
    directories = []
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if dir == name:
                directories.append(os.path.join(root, dir))
    if directories:
        return f"Found directories: {directories}"
    else:
        return f"No directories named '{name}' found in '{path}'"

def move_directory(src, dst):
    try:
        shutil.move(src, dst)
        return f"Directory '{src}' moved to '{dst}' successfully"
    except Exception as e:
        return f"An error occurred while moving the directory '{src}': {e}"

def main_menu():
    print("Directory Manager")
    print("========================")
    print("1. Display files in a directory")
    print("2. Make a directory")
    print("3. Delete a directory")
    print("4. Rename a directory")
    print("5. Search for a directory")
    print("6. Move a directory")
    print("7. Quit")

def handle_choice(choice):
    if choice == '1':
        directory = input("Enter the path of the directory: ")
        print(display_files(directory))
    elif choice == '2':
        name = input("Enter the name of the directory: ")
        path = input("Enter the path of the directory (optional): ")
        print(make_directory(name, path))
    elif choice == '3':
        directory = input("Enter the name of the directory: ")
        print(delete_directory(directory))
    elif choice == '4':
        old_name = input("Enter the current name of the directory: ")
        new_name = input("Enter the new name of the directory: ")
        print(rename_directory(old_name, new_name))
    elif choice == '5':
        name = input("Enter the name of the directory: ")
        path = input("Enter the starting path for the search: ")
        directories = search_directories(name, path)
        if directories:
            print("Found directories:")
            for directory in directories:
                print(directory)
        else:
            print("No directories found.")
    elif choice == '6':
        src = input("Enter the source path of the directory: ")
        dst = input("Enter the destination path of the directory: ")
        print(move_directory(src, dst))
    elif choice == '7':
        print("Exiting the program")
        sys.exit()
    else:
        print("Invalid choice. Try again.")

if __name__ == '__main__':
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        handle_choice(choice)