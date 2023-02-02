import os
import sys
import shutil

def display_files(directory):
    if not os.path.exists(directory):
        return f"\033[93mDirectory '{directory}' does not exist\033[93m"
    try:
        return os.listdir(directory)
    except Exception as e:
        return f"\033[91mAn error occurred while accessing the directory: {e}\033[91m"

def make_directory(name, path=None):
    if not name or any(char in name for char in "\\/:*?\"<>|"):
        return "\033[93mInvalid directory name. Please enter a valid name without any of the following characters: \\ / : * ? \" < > |\033[93m"
    
    if path:
        directory = os.path.join(path, name)
    else:
        directory = name
    try:
        os.mkdir(directory)
        return f"\033[32mDirectory '{directory}' created successfully\033[0m"
    except Exception as e:
        return f"\033[91mAn error occurred while creating the directory '{directory}': {e}\033[91m"

def delete_directory(directory):
    if not os.path.exists(directory):
        return f"\033[93mDirectory '{directory}' does not exist\033[93m"
    try:
        shutil.rmtree(directory)
        return f"\033[32mDirectory '{directory}' deleted successfully\033[32m"
    except Exception as e:
        return f"\033[91mAn error occurred while deleting the directory '{directory}': {e}\033[91m"

def rename_directory(old_name, new_name):
    if not os.path.exists(old_name):
        return f"\033[93mDirectory '{old_name}' does not exist\033[93m"
    if not new_name or any(char in new_name for char in "\\/:*?\"<>|"):
        return "\033[93mInvalid new directory name. Please enter a valid name without any of the following characters: \\ / : * ? \" < > |\033[93m"
    
    try:
        os.rename(old_name, new_name)
        return f"\033[32mDirectory '{old_name}' renamed to '{new_name}' successfully\033[32m"
    except Exception as e:
        return f"\033[91mAn error occurred while renaming the directory '{old_name}': {e}\033[91m"

def search_directories(name, path):
    if not os.path.exists(path):
        return f"\033[93mPath '{path}' does not exist\033[93m"
    
    directories = []
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if dir == name:
                directories.append(os.path.join(root, dir))
    if directories:
        return f"\033[32mFound directories: {directories}\033[32m"
    else:
        return f"\033[93mNo directories named '{name}' found in '{path}'\033[93m"

def move_directory(src, dst):
    try:
        shutil.move(src, dst)
        return f"\033[32mDirectory '{src}' moved to '{dst}' successfully\033[32m"
    except Exception as e:
        return f"\033[91mAn error occurred while moving the directory '{src}': {e}\033[91m"

def main_menu():
    print("\033[95m========================\033[95m")
    print("\033[0;36m   Directory Manager\033[0;36m")
    print("\033[95m========================\033[95m")
    print("\033[34m1. Display files in a directory\033[0m")
    print("\033[34m2. Make a directory\033[0m")
    print("\033[34m3. Delete a directory\033[0m")
    print("\033[34m4. Rename a directory\033[0m")
    print("\033[34m5. Search for a directory\033[0m")
    print("\033[34m6. Move a directory\033[0m")
    print("\033[34m7. Quit\033[0m")

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
        print("\033[93mInvalid choice. Try again.\033[93m")

if __name__ == '__main__':
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        handle_choice(choice)