import os

def display_files(directory):
    try:
        return os.listdir(directory)
    except:
        return "An error occurred while accessing the directory"

def make_directory(directory):
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

def main_menu():
    print("Directory Manager")
    print("========================")
    print("1. Display files in a directory")
    print("2. Make a directory")
    print("3. Delete a directory")
    print("4. Quit")

def handle_choice(choice):
    if choice == '1':
        directory = input("Enter the path of the directory: ")
        print(display_files(directory))
    elif choice == '2':
        directory = input("Enter the name of the directory: ")
        print(make_directory(directory))
    elif choice == '3':
        directory = input("Enter the name of the directory: ")
        print(delete_directory(directory))
    elif choice == '4':
        print("Exiting the program")
        sys.exit()
    else:
        print("Invalid choice. Try again.")

if __name__ == '__main__':
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        handle_choice(choice)