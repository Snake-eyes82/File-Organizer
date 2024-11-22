import os
import shutil
import tkinter as tk
from tkinter import filedialog


#"FUNCTIONS"
#Sorts the files in this manner
def sort_files(source_dir):  #sort_files(source_dir): This function takes the source directory path as input and performs the sorting.

    file_types = {

        #document files
        "documents": [".docx", ".pdf", ".txt"],
        "Presentation": [".ppt, .pptx, .odp, .ppsx"],
        "Spreadsheet": [".xls, .xlsx, .ods, .csv"],
        "Archive": [".zip, .rar, .7z, .tar.gz"],

        #image files
        "images": [".jpg", ".png", ".gif"],
        "Raster": [".jpg, .jpeg, .png, .gif, .bmp, .tif, .tiff"],
        "Vector": [".svg, .ai, .eps, .dxf"],

        #Video Files
        "videos": [".mp4", ".avi", ".mov"],

        #Audio files
        "audio": [".mp3", ".wav"],

        #Programming Files
        "Source Code": [".c, .cpp, .java, .py, .js, .html, .css"],
        "Executable": [".exe, .bin"],

        #Other File Types
        ##""others": []  # For files without a recognized extension"""
        "Font": [".ttf, .otf"],
        "Database": [".db, .sqlite"],
        "System": [".sys, .dll"],
        "Compressed": [".zip, .rar, .7z, .tar.gz"],
    }

    #searches through files
    for file in os.listdir(source_dir):
        src_file = os.path.join(source_dir, file)
        ext = os.path.splitext(file)[1].lower()

        #this shorts to file types
        #and changes the file directory and moves it to another directory
        for file_type, extensions in file_types.items():
            if ext in extensions:
                dest_dir = os.path.join(source_dir, file_type)
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
                shutil.move(src_file, dest_dir)
                break

            #this put's all other files not listed in the sort files into another folder that is not listed
        else:
            dest_dir = os.path.join(source_dir, "others")
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            shutil.move(src_file, dest_dir)

#This is the window user input function with a window
def get_user_input():
    root = tk.Tk()
    root.withdraw()
#this is the selection button
    source_dir = filedialog.askdirectory(title="Select Source Directory")
    if not source_dir:
        return

    sort_files(source_dir)


#"MAIN SCRIPT"
if __name__ == "__main__":
    get_user_input()