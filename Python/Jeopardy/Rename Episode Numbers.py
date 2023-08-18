# Fairly limited script
# Given a list of episode numbers in a text file, and a folder containing video files
# This script can be used to rename the filenames based off the the supplied text file
# August 15, 2023

import os

def rename_files(current_names_file, new_names_file, folder_path):
    # Read the current names and new names from the text files
    with open(current_names_file, 'r') as current_file:
        current_names = current_file.read().splitlines()

    with open(new_names_file, 'r') as new_file:
        new_names = new_file.read().splitlines()

    # Check if the number of current names and new names match
    if len(current_names) != len(new_names):
        print("Error: Number of current names and new names do not match.")
        return

    # Rename files in the folder
    for current_name, new_name in zip(current_names, new_names):
        current_path = os.path.join(folder_path, current_name)
        new_path = os.path.join(folder_path, f"Jeopardy! - " + new_name + ".mkv")
        
        try:
            os.rename(current_path, new_path)
            print(f"Renamed '{current_name}' to '{new_name}'.")
        except FileNotFoundError:
            print(f"File '{current_name}' not found.")

if __name__ == "__main__":
    current_names_file = r"C:\Users\Noah-PC\Documents\StreamFab\StreamFab\Temp\outputTemp - Copy\test\name_list.txt"  # Change to your current names text file
    new_names_file = r"C:\Users\Noah-PC\Documents\StreamFab\StreamFab\Temp\outputTemp - Copy\test\ken jenning episode list from tvmate.txt"  # Change to your new names text file
    folder_path = r"C:\Users\Noah-PC\Documents\StreamFab\StreamFab\Temp\outputTemp - Copy\test\FINAL"  # Change to the folder path

    rename_files(current_names_file, new_names_file, folder_path)
