import os
from pathlib import Path
directory_name = "dir1"

os.mkdir(directory_name)

nested_directory = "dir2/dir3"
os.makedirs(nested_directory)

direc_path = Path("dir4")

direc_path.mkdir()

nested_direc_path = Path("dir5/dir6")

nested_direc_path.mkdir(parents=True, exist_ok=True) #exist_ok parametr prevents errors if the file already exists


