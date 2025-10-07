import os
if(not os.path.exists("data")):
    os.mkdir("data")                # To create Folder


# for i in range(100):                   
#     os.mkdir(f"data/day{i+1}")    # To create range of files at once.

# for i in range(100):
#     os.rename(f"data/Tutorial{i+1}",f"data/Tutorial  {i+1}")     # To rename the files in the folder.

# folders = os.listdir("data")      # To check list of the folders from the main folder
# #print(folders)         # Printing all folders

# for fld in folders:
#     print(fld)
#     print(os.listdir(f"data/{fld}"))   # Checking files inside folders.

#os.getcwd()     # Getting the directory name.

#os.chdir("/Users") # Used to change directory

#print(os.listdir()) # Will give all the folder name from that folder

#os.rmdir('data/Tutorial  2')  # Delete files 

#os.rename('data/Tutorial  3','data/Your_turn') # Rename but give folder name 

#print(os.stat('data'))  # It gives all the information ofo the file.

#print(os.stat('data').st_size) # It gives the total size of the data folder in bytes.

# mod_time=os.stat('data').st_mtime # It returns best modification time.
# from datetime import datetime
# print(datetime.fromtimestamp(mod_time)) # This will return the modification time in human readable format.


## Used to search files from the folders
#for dirpath, dirnames, filenames in os.walk("/Users/Gaurav Yeskar/OneDrive/Desktop/ALL_GITS/python"):
    print("Current Path: ",dirpath)
    print("Directories: ",dirnames)
    print("Files: ",filenames)
    print()

# print(os.path.basename("/data/Tutorial  4")) # Gives basename of the file
# print(os.path.dirname('/data/Tutorial  4')) # Gives directory name 
# print(os.path.split('/data/Tutorial  4'))  #Seperates both the dir and the files
# print(os.path.exists('data/Tutorial  4')) # Checks if the path is there inn the folder then it will return true
# print(os.path.isdir('data/Tutorial  4'))  # returns true if its a direc
# print(os.path.isfile('data/Tutorial  4')) # Returns true if its a file.
# print(os.path.splitext('data/tutorial.txt'))

#print(os.rename(f"data/Tutorial  4","tutorial.txt"))
#print(os.listdir())   # gives all the list ofo files in the directory

#os.makedirs("This/that")  # Makes files and folders at the same time.

#print(os.environ.get("Path"))

#print(os.name)
#print(os.cpu_count())

#print(os.mkdir("Calender"))
#print(os.mkdir("Calender/File1"))

# import calendar
# #print(calendar.isleap(2033))

# print(calendar.weekday(2025,9,24))
# print(calendar.APRIL)
# print(calendar.SEPTEMBER)
# print(calendar.day_abbr)
# print(calendar.day_abbr[calendar.SUNDAY])

import math
print(math.sqrt(4))