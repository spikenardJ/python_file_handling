# Question 1: Exploring Python's OS Module

# Task 1: Directory Inspector:

import os
import sys
from termcolor import colored

def list_directory_contents():
    while True:
        path = input("Enter your directory path to see the contents: ").strip()
        print(f"Received path: {path}") # Debugging output

        if not os.path.exists(path): # Checking path existance
            print(f"The path '{path}' does not exist. Please try again.")
            continue

        if not os.path.isdir(path):  # Checking if path is a directory
            print(f"The path '{path}' is not a valid directory. Please try again.")
            continue
        
        try:
            path_contents = os.listdir(path)
            if not path_contents:
                print("The directory is empty.")
            else:
                print(colored("\nPath Contents:\n", "cyan", attrs=["bold"]))
                for item in path_contents:
                    full_path = os.path.join(path, item)  # Join directory path with item
                    if os.path.isdir(full_path):
                        print(colored(f"Directory: ", "grey", attrs=["bold"]), end=" ") # Print directory (for folders)
                        print(colored(f"{item}"))
                    elif os.path.isfile(full_path):
                        print(colored(f"File: ", "red", attrs=["bold"]), end=" ") # Print files
                        print(colored(f"{item}"))
        except PermissionError:
            print("Permission denied, please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

list_directory_contents()
