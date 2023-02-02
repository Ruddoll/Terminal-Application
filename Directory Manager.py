import sys
import os

def display_files(directory):
    try:
        files = os.listdir(directory)
        for file in files:
            print(file)
    except:
        print("An error occured while accessing the directory")
        sys.exit()

def main():
    print("Directory Manager")
    print("========================")
    print("1. Display files in a directory")
    print("2. Quit")

    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        directory = input("Enter the directory path: ")
        display_files(directory)
    elif choice == '2':
        sys.exit()
    else:
        print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()