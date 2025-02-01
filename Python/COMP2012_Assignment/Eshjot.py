# Creating a Python application which performs various tasks 

import os 
# Creating a variable file and assigning it value
file = "file.txt"

# Checking if the file exists or not

if os.path.exists(file):
    with open(file, "r") as datafile:  #datafile is an alternate name for "file"
        content = datafile.read()    # Reading file's content
        if content.strip():       
            print("Displaying File's content")   # verifying the file is empty or not
            print(content)
        else:
            print("File is empty")

else:       
    print("Sorry, the file does not exist. Creating a new file")  # If the file does not exist, it will create a new file
    student_name ="Eshjot Singh"        # Content of file to be displayed in file.txt
    student_id = 500227052
    with open(file, "w") as datafile:   # file opening in write mode to add above mentioned content
        datafile.write(f"Name: {student_name} \n")
        datafile.write(f"Student ID: {student_id} \n")

        with open(file, "r") as datafile:  # again file opening in read mode
            print("Content added in file")
            print(datafile.read())