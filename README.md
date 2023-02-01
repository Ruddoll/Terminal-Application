# **Directory Manager**

Directory Manager is a Python script that provides several functionalities to manage directories in a computer system. It is an easy-to-use program that allows you to display the contents of a directory, create new directories, delete existing directories, search for a specific directory, move a directory to a different location and rename a directory.

## **Repository and Video links**

[GitHub link](https://github.com/Ruddoll/Terminal-Application)
[Youtube Video](https://youtu.be/8oa_Yr0gfvA)


## **Features**



1. Display files in a directory

The display_files function allows users to see a list of files in a directory. The function takes the directory path as an argument and provides a list of the files in the directory using the os.listdir method.



2. Make a directory

The make_directory function enables users to make a new directory. The function takes two arguments: name (the name of the directory) to be created and path (the path of the directory). If the path argument is not provided, the directory will be created in the current working directory. The function creates the directory using the os.mkdir method.



3. Delete a directory

The delete_directory function allows users to delete a directory. The function takes the directory path as an argument and deletes the directory using the os.rmdir method.



4. Search for a directory

The search_directories function allows users to search for a directory in the file system. The function takes two arguments: name which is the name of the directory to be searched for, and path which is the starting path for the search. The function uses the os.walk method to perform a recursive search and returns a list of directories that match the search criteria.



5. Move directory location

The move_directory function enables users to move a directory to a new location. The function takes two arguments: src which is the source path of the directory, and dst which is the destination path. The function uses the shutil.move method to move the directory to the new location.



6. Rename directory

The rename_directory function allows users to rename a directory. The function takes two arguments: src which is the source path of the directory, and dst which is the new name for the directory. The function uses the os.rename method to rename the directory.

The script provides a main menu for users to choose from the different functionalities. The handle_choice function takes **the user's** input **and calls the appropriate function to** perform the requested operation. The script will continue to run until the user chooses to quit.


## **Requirements**



* Python 3.x
* OS library
* Sys library


## **Usage**



1. Download and extract the script file.
2. Open the terminal or command prompt.
3. Navigate to the folder where the script file is located.
4. Run the script file using the command python directory_manager.py.
5. The program will display the main menu with the following options:
    * Display files in a directory
    * Make a directory
    * Delete a directory
    * Search for a directory
    * Move a directory to a different location
    * Rename a directory
6. Enter the number corresponding to the desired operation and follow the prompts.


## **Code Style**

This application code adheres to the following conventions as it follows the  PEP 8 - Style Guide for Python Code:



* Indentation: 4 spaces are used for indentation.
* Line Length: Maximum line length is 79 characters.
* Naming Conventions: Variables, functions and modules are named in snake_case. Classes are named in CamelCase.
* Imports: Imports are sorted alphabetically and grouped logically.
* Spaces: Surround binary and ternary operators with a single space on either side for clarity.
* Comments: Inline comments are used to explain the code. Block comments are used to explain the logic.
* Exceptions: Exception messages are written in a meaningful and concise manner.

Reference:



* <span style="text-decoration:underline;">Python.org. (2013). PEP 8 -- Style Guide for Python Code. [online] Available at: [https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/)**.**</span>


## **Implementation Plan**


### Feature 1: Display files in a directory



1. Create a function display_files that takes in a directory path as a parameter.
2. Use the os.listdir method to list all files in the given directory.
3. Return the list of files.
4. Implement the option to call the display_files function in the main menu.
5. Test the implementation by providing various directory paths and verifying the correct files are displayed.


### Feature 2: Make a directory



1. Create a function make_directory that takes in a directory name and an optional path parameter.
2. If the path parameter is provided, use os.path.join to join the path and the name to create the full directory path.
3. Use the os.mkdir method to create the directory.
4. Return a success message upon successful creation of the directory.
5. Implement the option to call the make_directory function in the main menu.
6. Test the implementation by creating multiple directories with and without paths and verifying the directories are created.


### Feature 3: Delete a directory



1. Create a function delete_directory that takes in a directory path.
2. Use the os.rmdir method to delete the directory.
3. Return a success message upon successful deletion of the directory.
4. Implement the option to call the delete_directory function in the main menu.
5. Test the implementation by deleting multiple directories and verifying the directories are deleted.


### Feature 4: Search for a directory



1. Create a function search_directories that takes in a directory name and a starting path.
2. Use the os.walk method to traverse the file system and find all directories with the given name.
3. Return a list of all the directories with the given name.
4. Implement the option to call the search_directories function in the main menu.
5. Test the implementation by searching for directories with different names in various starting paths and verifying the correct directories are returned.


### Feature 5: Move directory location



1. Create a function move_directory that takes in the current directory path and the new desired directory path.
2. Implement the logic to move the directory from its current location to the new location.
3. Return a success message upon successful movement of the directory.
4. Implement the option to call the move_directory function in the main menu.
5. Test the implementation by moving directories to different locations and verifying the directories have been moved successfully.


### Feature 6: Rename a directory



1. Create a function rename_directory that takes in the current directory path and the new desired directory name.
2. Use the os.rename method to rename the directory.
3. Return a success message upon successful renaming of the directory.
4. Implement the option to call the rename_directory function in the main menu.
5. Test the implementation by renaming directories to different names and verifying the directories have been renamed successfully.

This implementation plan can be tracked using a project management platform such as Trello or Asana, with a task created for each of the 5 steps, a deadline set for completion, and updates made as each step is completed.


### Order of Priority

I would prioritise the implementation of the features in the following order:



1. Display files in a directory
2. Make a directory
3. Delete a directory
4. Search for a directory
5. Move directory location
6. Rename a directory