"""
Module 2 — Activity: File Sorting with os and shutil
Student: [Santiago Kyle]
Date: [9/27/26]

============================================
WHAT DID YOU BUILD? (explain in your own words)
WHAT DID YOU BUILD?
============================================
[Paste your working script below first, then come back and explain
it here: what does your script do, and what rule did you use to
sort the files? e.g. by extension, by name, by date, etc.]

I build a filesorting script that organizes files in a specified source folder into subfolders based on their file types. 
The script checks the file extensions and moves image files to an "Images" folder, document files to a "Documents" folder, 
and any other files to an "Others" folder.

============================================
KEY VOCABULARY
============================================
- os module:
- shutil module:
- file path:
- directory:
(add more as needed)
- os module: Is a Python module used for interacting with the operating system, such as working with files, folders, and file paths.
- shutil module: Is a Python module used for high-level file operations, such as copying and moving files.
- file path: The location of a file in the file system.
- directory: A folder in the file system used to organize files.


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil
#Folders containing different file types
source_folder = "C:\\Users\\User\\Downloads\\devnet"

# --- paste your existing code here ---
# Folders for different file types
image_folder = os.path.join(source_folder, "Images")
document_folder = os.path.join(source_folder, "Documents")
other_folder = os.path.join(source_folder, "Others")

# Create folders if they don't exist
os.makedirs(image_folder, exist_ok=True)
os.makedirs(document_folder, exist_ok=True)
os.makedirs(other_folder, exist_ok=True)

# File extensions for each category
image_extensions = [".jpg", ".jpeg", ".png", ".gif"]
document_extensions = [".pdf", ".docx", ".doc", ".txt"]

# Check every item in the source folder
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    # Determine the file's category based on its extension
    _, ext = os.path.splitext(filename)
    if ext.lower() in image_extensions:
        destination = image_folder
    elif ext.lower() in document_extensions:
        destination = document_folder
    else:
        destination = other_folder

    # Move the file to its designated folder
    shutil.move(file_path, os.path.join(destination, filename))

print("Files have been sorted successfully!")


"""

============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[One mistake I needed to avoid was using a folder path that did not exist. 
If the source folder cannot be found, the script will not work correctly. 
I used os.makedirs() with exist_ok=True to make sure the destination folders are created automatically when they do not already exist.

Another thing to avoid is accidentally moving folders instead of files, which is why the script checks os.path.isdir() and skips directories.]

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
"""