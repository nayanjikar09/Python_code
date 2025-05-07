#it use to create multiple folde at a time
#also use to rename the folder
#we can perform multiple folder operation on os module
import os 

os.mkdir("data")
for i in range(1, 100):
    os.mkdir(f"daya?day{i+1}")
    
    folders==os.listdir("data/{folders}")
    print(folders)
    
    for folders in folders:
        print(folders)