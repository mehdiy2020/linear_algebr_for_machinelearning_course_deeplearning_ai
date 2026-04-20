# Start of a new Python program
import os
def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, "w") as file:
    file.write(comments)
    
  filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program2.py"))

import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(directory)

  # Create the new file inside of the new directory
  os.chdir(directory)
  with open (filename, "w") as file:
    pass

  # Return the list of files in the new directory
  return os.listdir()

print(new_directory("PythonPrograms", "script.py"))

import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename, "w") as file:
    timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  out = datetime.datetime.fromtimestamp(timestamp)
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{0}".format(str(out)[:10]))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd


comments = "# Start of a new Python program"
with open("something.txt", "w") as file:
  file.write(comments)

filesize = os.path.getsize("something.txt")
filesize

os.getcwd()

import os
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
  relative_parent = os.path.join("/", os.getcwd())

  # Return the absolute path of the parent directory
  return os.path.abspath(relative_parent)

print(parent_directory())

# Parsing a file means analyzing a file's content to corretly structure the data
# If we know te format of the data, we can separate it into understandable parts

import csv
f = open("csv_file.txt")
csv_f = csv.reader(f)
for row in csv_f:
  name, phone, role = row
  print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
f.close()

import csv

hosts = [["workstation.local", "192.168.25.46"],["webserver.cloud", "10.2.5.6"]]
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
#the following command should be used in the terminal
#cat software.csv 
#Output name,version,status,users
#MailTree,5.34,production,324
#CalDoor,1.25.1,beta,22
#Chatty Chicken,0.34,alpha,4
with open('software.csv') as software:
    reader = csv.DictReader(software) # Truns each row into a dictionary and we can access data using the column names
    for row in reader:
      print(("{} has {} users").format(row["name"], row["users"]))
      
users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, 
 {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, 
  {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]
with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader() # Creates headers or field names 
    writer.writerows(users) # add the info relevant to each field
    
    
import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename) as file:
    # Read the rows of the file
    rows = csv.reader(file)
    # Process each row
    for row in rows:
      name, color, type = row
      # Format the return string for data rows only
      if name != "name" and color != "color" and type != "type":
        return_string += "a {} {} is {}\n".format(name, color, type)
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))

import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")


# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename) as file:
    # Read the rows of the file into a dictionary
    reader = csv.DictReader(file)
    # Process each item of the dictionary
    for row in reader:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string


#Call the function
print(contents_of_file("flowers.csv"))