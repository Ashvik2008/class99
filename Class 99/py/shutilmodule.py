#shutil.copy() method
import shutil

source="C:/Python/99/file1.txt"
destination="C:/Python/99/folder1/folder2/file1.txt"

try:
    shutil.copy(source,destination)
    print("File copied successfully")

except shutil.SameFileError:
    print("Source and destination represents the same file.")

except PermissionError:
    print("Permission denied")
except:
    print("Error occurred while copying file")

#--------------------------------------------------------------------------------

#to know the permission of the file
import os
source="Sample_Folder/Sample1.txt"
perm=os.stat(source).st_mode
print(perm)

#--------------------------------------------------------------------------------

#if destination is a directory
import os
import shutil
source="Folder_2/Sample.txt"
destination="Folder_1"

dest=shutil.copy(source,destination)

print(os.listdir(destination))
print("destination path:",dest)

#--------------------------------------------------------------------------------

#shutil.copyfile
#copy the contents of the source file to destination file

source="Folder_1/Temp.txt"
destination="Folder_2/Temp.txt"

dest=shutil.copyfile(source,destination)

#--------------------------------------------------------------------------------

import shutil

source="Folder_1/Temp.txt"
destination="Sample_Folder"

try:
   shutil.copyfile(source,destination)
   print("file copied successfully")
except shutil.SameFileError:
    print("source and destination represents the same file")
except IsADirectoryError:
    print("destination is a directory")
except PermissionError:
    print("Permission denied")
except:
    print("Error occurred while copying file")

#this code return an error
#------------------------------------------------------