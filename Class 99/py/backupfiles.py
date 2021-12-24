# Python program to explain shutil.copy() method 

# importing shutil module 
import shutil 
  
source = "Folder_1/Sample.txt"
destination = "Folder_2/Sample.txt"
  
# Copy the content of 
# source to destination 
dest = shutil.copy(source, destination) 
  
# Print path of newly 
# created file 
print("Destination path:", dest) 