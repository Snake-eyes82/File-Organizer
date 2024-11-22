import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import logging

# Configure logging
logging.basicConfig(filename='file_sorter.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#"FUNCTIONS"
#Sorts the files in this manner
def sort_files(source_dir):  #sort_files(source_dir): This function takes the source directory path as input and performs the sorting.
    file_types = {

        #document files
        "documents": [".docx", ".pdf", ".txt"],
        "Presentation": [".ppt", ".pptx", ".odp", ".ppsx"],
        "Spreadsheet": [".xls", ".xlsx", ".ods", ".csv"],
        "Archive": [".zip", ".rar", ".7z", ".tar.gz"],

        # image files
        "images": [".jpg", ".png", ".gif"],
        "Raster": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tif", ".tiff"],
        "Vector": [".svg", ".ai", ".eps", ".dxf"],

        # Video Files
        "videos": [".mp4", ".avi", ".mov"],

        # Audio files
        "audio": [".mp3", ".wav"],

        # Programming Files
        "Source Code": [".c", ".cpp", ".java", ".py", ".js", ".html", ".css"],
        "Executable": [".exe", ".bin"],

        # Other File Types
        "Font": [".ttf", ".otf"],
        "Database": [".db", ".sqlite"],
        "System": [".sys", ".dll"],
        "Compressed": [".zip", ".rar", ".7z", ".tar.gz"]
    }

    root = tk.Tk()
    root.title("File Sorter")

    # Create a Treeview to display files and their proposed destinations
    tree = ttk.Treeview(root)
    tree["columns"] = ("file", "destination")
    tree.heading("#0", text="")
    tree.heading("file", text="File")
    tree.heading("destination", text="Destination")
    tree.pack(fill="both", expand=True)

    #for root, dirs, files in os.walk(source_dir):
    for root, _, files in os.walk(source_dir):  # Ignore directories
        for file in files:
            src_file = os.path.join(root, file)
            ext = os.path.splitext(file)[1].lower()

            for file_type, extensions in file_types.items():
                if ext in extensions:
                                        # Prompt user for custom folder name
                    custom_dir_name = filedialog.asksaveasfilename(initialdir=source_dir, title=f"Choose Destination Folder for {file_type} Files")
                    if custom_dir_name:
                        dest_dir = os.path.join(source_dir, custom_dir_name)
                    dest_dir = os.path.join(source_dir, file_type)
                    if not os.path.exists(dest_dir):
                        os.makedirs(dest_dir)

                    # Prompt user before moving critical files
                    if file in ["system32", "Windows", "Program Files"]:
                        if not messagebox.askyesno("Confirm Move", f"Move {file} to {dest_dir}?"):
                            continue

                    # Prompt user to choose destination folder
                    dest_folder = filedialog.askdirectory(initialdir=dest_dir, title=f"Choose Destination for {file}")
                    if dest_folder:
                        shutil.move(src_file, dest_folder)
                        logging.info(f"Moved {src_file} to {dest_folder}")
                    else:
                        logging.warning(f"User canceled move for {src_file}")
                    break

            else:
                dest_dir = os.path.join(source_dir, "others")
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
                shutil.move(src_file, dest_dir)
                tree.insert("", "end", values=(file, dest_dir))
                logging.info(f"Moved {src_file} to {dest_dir}")

    def confirm_move():
        for item in tree.get_children():
            file = tree.item(item)['values'][0]
            dest_dir = tree.item(item)['values'][1]
            src_file = os.path.join(source_dir, file)
            shutil.move(src_file, dest_dir)
            logging.info(f"Moved {src_file} to {dest_dir}")
        root.destroy()

    confirm_button = tk.Button(root, text="Confirm and Move", command=confirm_move)
    confirm_button.pack()

    root.mainloop()

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