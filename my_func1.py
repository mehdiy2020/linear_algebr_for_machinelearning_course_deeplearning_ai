import shutil
import psutil

def check_disk_usage(disk):
  du = shutil.disk_usage(disk)
  free = du.free/du.total * 100
  return free > 20

def check_cpu_usage():
  usage = psutil.cpu_percent(1)
  return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
  print("Error!")
else:
  print("Everything is OK!")

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
    
    next(rows)
    # Process each row
    for row in rows:
      name, color, type = row
      # Format the return string for data rows only
    
    return_string += "a {} {} is {}\n".format(name, color, type)
  return return_string

#Call the function
print(contents_of_file("flowers1.csv"))

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
index = log.index("[")
print(log[index+1:index+6])


import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])
print(result)

result

import re
def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

print(re.search(r"[a-zA-Z]", "This is a sentence with spaces."))
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))
print(re.findall(r"cat|dog", "I like both dogs and cats."))

print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"o+l+", "goyldfish"))
print(re.search(r"o+l+", "woolly"))

print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))


print(re.search(r"[a]{2,}[A]{2,}", "banana"))

print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com"))

print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w* *", "This is an example"))

import re
print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbaijan"))
print(re.search(r"^A.*?a", "Australia"))

pattern = r"^[a-zA-Z_][a-zA-Z0-9_\s']*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isn't a valid variable"))
print(re.search(pattern, "my_variable1"))
print(re.search(pattern, "2my_variable1"))

import re

text = "/users/123/extra/stuff/"

print(re.search(r"^/(.+)/([^/]+)/$", text))       # captures both
print(re.search(r"^/(.+)/[^/]+/$", text))         # captures only first

print(re.search(r"^/(.+)/$", text))         # captures only first
print(re.search(r"^/(.+)/", text))         # captures only first
def check_web_address(text):
  pattern = r"[a-zA-Z0-9_.+-]+\.(com|org|US|info|edu)$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # 

def check_time(text):
  pattern = r"^[1-9][0-2]?:[0-5][0-9]\s?(am|pm|PM|AM)"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False
print(check_time("6:02 am")) # True
print(check_time("6:02km")) # False


def contains_acronym(text):
  pattern = r"[a-zA-Z\s]+\([A-Z0-9][a-zA-Z0-9]+\).*"
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True

def correct_function(text):
  result = re.search(r".+?\s\d{5}(-\d{4})?.*", text)  # Corrected regex pattern with space
  return result is not None

def check_zip_code(text):
  return correct_function(text)  # Call the correct_function

# Call the check_zip_code function with test cases
print(check_zip_code("The zip codes for New York are 10001 thru 11104."))  # True
print(check_zip_code("90210 is a TV show"))  # False (no space before 90210)
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001."))  # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9."))  # False


import re
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])
"{} {}".format(result[2], result[1])

def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name("Lovelace, Ada")
rearrange_name("Ritchie, Dennis")

def rearrange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name("Hopper g_. s, Grace M.")

print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared")) # find the first match

print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))

re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared")

print(re.findall(r"\w{5,10}", "I really like strawberries"))

print(re.findall(r"\w{5,}", "I really like strawberries"))

print(re.search(r"s\w{,20}", "I really like strawberries"))

def long_words(text):
  pattern = r"\w{7,}"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
result = re.search(regex, "A completely different string that also has numbers [34567]")
print(result[1])

def extract_pid(log_line):
    regex = r"(\[(\d+)\]):\s([A-Z]*)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[2], result[3])
  
print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)

print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)


regex = r"(\[(\d+)\]):\s([A-Z]*)"
result = re.search(regex, "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")
print(result)
result[0]

re.split(r"[.?!]", "One sentence. Another one? And the last one!")

re.split(r"([.?!])", "One sentence. Another one? And the last one!")

re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com")

re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")

re.split(r"the|a", "One sentence. Another one? And the last one!")

re.sub(r"([A-Z])\.\s+(\w+)", r"Ms. \2", "A. Weber and B. Bellmas have joined the team.") # Backrefrences

# Lookahead
# If the regex was r”(Test\d)-(?=Passed)” and the string was “Test1-Passed, Test2-Passed, Test3-Failed, Test4-Passed, Test5-Failed” the output would be:

# Test1, Test2, Test4

def transform_record(record):
  new_record = re.sub(r"(\d{3}-?\d{3}?-?\d{4,}?)", r"+1-\1", record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

def multi_vowel_words(text):
  pattern = r"\w+[aeiou]{3,}\w+"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

def transform_comments(line_of_code):
  result = re.sub(r"[#]+", r"//", line_of_code)
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable"))


def convert_phone_number(phone):
  result = re.sub(r"(\d{3})-(\d{3})-(\b\d{4}\b)", r"(\1) \2-\3", phone)
  return [result]

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300"))

def parse_city_state(text):
 pattern = r"([\w]+)[,.]\s([\w]+)" #enter the regex pattern here
 result = re.search(pattern, text) #enter the re method  here
 if len(result) != 2:
  return ""
 return result[2]#return the correct capturing group


print(parse_city_state("Hamilton, MN")) # should return MN
print(parse_city_state("Albuquerque, New Mexico")) # should return New Mexico
print(parse_city_state("Portland. Oregon")) # should return Oregon

pattern = r"([\w]+)[,.]\s([\w]+)" #enter the regex pattern here
result = re.search(pattern, "Hamilton, MN") 
print(result[2])
len(result)
pattern = r"[,.]" #enter the regex pattern here
result = re.split(pattern, "Hamilton, MN") 
print(result)
len(result)

def find_isbn(list):
  pattern = r"\b\d{3}\b-\d{1}-\d{2}-(\d{6})-\d{1}" #enter the regex pattern here
  result = re.search(pattern, list) #enter the re method  here
  if result is None:
    return ""
  return result[1] #return the correct capturing group


print(find_isbn("123-4-12-098754-0")) # Should return 098754
print(find_isbn("223094-AB-30")) # result should be blank
print(find_isbn("1123-4-12-098754-0")) # result should be blank

def secure_website_domain(website):
 pattern = r"https://[\w]+\.([\w]+)\.[com|co]" # enter the regex pattern here
 result = re.search(pattern, website) # enter the re method here
 if result is None:
  return ""
 return result[1]# enter the correct capturing group


print(secure_website_domain("http://www.text.com")) #Should return nothing
print(secure_website_domain("https://www.text.com")) #Should return text
print(secure_website_domain("http://www.text.co")) #Should return nothing
print(secure_website_domain("https://www.text.co")) #Should return text