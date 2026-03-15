import shutil
import os

source = "path/main.py"
destination = "path/main2.py"

dest = shutil.copy(source, destination)

print("Destination path:", dest)




source = "path/main.py"
   
destination = "path/gfg/"
  
# Copy the content of 
# source to destination 
dest = shutil.copy(source, destination) 
  

# Print path of newly  
# created file 
print("Destination path:", dest)


file_path = "ex.txt"

if os.path.exists(file_path):
    os.remove(file_path)
else:
    print("this file doesn't exist")
