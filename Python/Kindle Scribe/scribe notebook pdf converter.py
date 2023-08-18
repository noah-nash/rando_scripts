# This script requires the use of a the KFX-Input plugin for Calibre, found on Mobileread.
# Convert Kindle Scribe notebook files into epub, and later pdf files. 
# Margins are set to a half inch, passed though in the calibre command.
# August 10, 2023

import os
import subprocess

# Replace this with the path to your Calibre debug and conver executables
calibre_debug_executable = r"C:\Program Files\Calibre2\calibre-debug.exe"
calibre_convert_executable = r"C:\Program Files\Calibre2\ebook-convert.exe"

# Path to the directory containing the folders
notebook_directory = r"D:\<Scribe root folder>\.notebooks"

# Loop through each folder in the base directory
for folder_name in os.listdir(notebook_directory):
    folder_path = os.path.join(notebook_directory, folder_name)
    
    # Check if the item is a directory. Don't run if not a notebook directory
    # Thumbnail, and personal document files are excluded.
    if os.path.isdir(folder_path) and folder_name != ".backup" and folder_name != "thumbnails" and "!!PDOC!!" not in folder_name and "!!EBOK!!" not in folder_name:
        # Construct the command
        command = [calibre_debug_executable, "-r", "KFX Input", "--", folder_path, f"{folder_name}.epub"]
        
        # Run the command
        subprocess.run(command)
        
        epub_file = os.path.join(notebook_directory, f"{folder_name}.epub")
        pdf_file = os.path.join(notebook_directory, f"{folder_name}.pdf")
        ebook_convert_command = [
            calibre_convert_executable,
            epub_file,
            pdf_file,
            "--pdf-page-margin-top", "36",
            "--pdf-page-margin-bottom", "36",
            "--pdf-page-margin-left", "36",
            "--pdf-page-margin-right", "36"
        ]
        
        # Run the command
        subprocess.run(ebook_convert_command)
