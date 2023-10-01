# Requirements: This script requires the use of a the KFX-Input plugin for Calibre, found on Mobileread.
#
# Usage: Convert Kindle Scribe notebook files into epub, and later pdf files. 
# Margins are set to a half inch, passed though in the calibre command.
# October 1, 2023

import os
import subprocess

# Replace this with the path to your Calibre debug and conver executables
calibre_debug_executable = r"C:\Program Files\Calibre2\calibre-debug.exe"
calibre_convert_executable = r"C:\Program Files\Calibre2\ebook-convert.exe"

# Path to the directories. Where notebook_directory is where they are stored on Kindle.
notebook_directory = r"C:\<Scribe root folder>\.notebooks"
output_directory = r"C:\<PC root folder>\Kindle_Scribe_PDF_Files"

# Temporary directory for epub files
epub_directory = output_directory + r"\scribePython_temp_epub_files"
if not os.path.exists(epub_directory):
    os.mkdir(epub_directory)


# Loop through each folder in the base directory
print("Script will begin processing your files...")

for folder_name in os.listdir(notebook_directory):
    folder_path = os.path.join(notebook_directory, folder_name)
    
    # Check if the item is a directory. Don't run if not a notebook directory
    # Thumbnail, and personal document files are excluded.
    if os.path.isdir(folder_path) and len(folder_name) == 36 and folder_name != ".backup" and folder_name != "thumbnails" and "!!PDOC!!" not in folder_name and "!!EBOK!!" not in folder_name:
        # Construct the inital command to convert to ePub.
        command = [calibre_debug_executable, "-r", "KFX Input", "--", folder_path, os.path.join(epub_directory, f"{folder_name}.epub")]
        
        # Run the command
        subprocess.run(command)
        
        # Construct the second command to convert ePub to PDF.
        epub_file = os.path.join(epub_directory, f"{folder_name}.epub")
        pdf_file = os.path.join(output_directory, f"{folder_name}.pdf")
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
        
# Prompt the user if they would like to delete the intermediary ePub files.
user_input = input("Would you like to delete .epub files? WARNING THIS WILL DELETE ALL EPUB FILES IN 'scribe_temp_epub_files' DIRECTORY (Y/N): ").strip().lower()
if user_input == "y":
    try:
        # Loop through all ePub files in notebook directory, and delete.
        for epub_file in os.listdir(epub_directory):
			# As of 2023, the filename for scribe notebook files are 41 characters long.
        	if epub_file.endswith(".epub") and len(epub_file) == 41:
                    file_path = os.path.join(epub_directory, epub_file)
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                    print("Deletion process completed. Script has completed.")
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("Deletion will not occur. Script has completed.")
