import os
import sys

try:
    import termcolor
except ImportError:
    os.system("pip install termcolor")
    import termcolor

def display_files(directory):
    try:
        return os.listdir(directory)
    except:
        return "An error occurred while accessing the directory"

def make_directory(name, path=None):
    if path:
        directory = os.path.join(path, name)
    else:
        directory = name
    try:
        os.mkdir(directory)
        return "Directory created successfully"
    except:
        return "An error occurred while creating the directory"

def delete_directory(directory):
    try:
        os.rmdir(directory)
        return "Directory deleted successfully"
    except:
        return "An error occurred while deleting the directory"

def search_directories(name, path):
    directories = []
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if dir == name:
                directories.append(os.path.join(root, dir))
    return directories

def main_menu():
    print("Directory Manager")
    print("========================")
    print("1. Display files in a directory")
    print("2. Make a directory")
    print("3. Delete a directory")
    print("4. Search for a directory")
    print("5. Quit")

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
        name = input("Enter the name of the directory: ")
        path = input("Enter the starting path for the search: ")
        directories = search_directories(name, path)
        if directories:
            print("Found directories:")
            for directory in directories:
                print(directory)
        else:
            print("No directories found.")
    elif choice == '5':
        print("Exiting the program")
        sys.exit()
    else:
        print("Invalid choice. Try again.")

if __name__ == '__main__':
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        handle_choice(choice)


