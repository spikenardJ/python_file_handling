# Question 1: Exploring Python's OS Module

# Task 1: Directory Inspector:

import os

def list_directory_contents(path): # List and print all files and subdirectories in the given path
    while True:
        path = input("Enter your directory path to see the contents: ")
        path_contents = os.listdir(path)
        try:
            for path in path_contents:
                print(f"Here is the contents of your path: \n{path}")
        except FileNotFoundError:
            print("File was not found, please try again")
            return
        list_directory_contents(path)