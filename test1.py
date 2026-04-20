print("Hello World!!!!")

my_comment=f"I am more experienced in python to be required ti install python from scratch, please accept it as i am woring on VSCode!"

print(my_comment)


print(ord("\n"))

test1 = b'asssa'
type(test1)
test2 = 'asssa'
type(test2)

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen(url='http://data.pr4e.org/romeo.txt')

for line in fhand:
  print(line.decode().strip())

counts = dict()
for line in fhand:
  words = line.decode().strip().split()
  for word in words:
    counts[word] = counts.get(word, 0) + 1
    
print(counts)

fhand = urllib.request.urlopen(url='http://www.dr-chuck.com/page1.htm')

for line in fhand:
  print(line.decode().strip())
  
import re

for line in fhand:
  if 'href' in line.decode().strip() and re.search(r'[a-z]+:', line.decode().strip()):
     print(re.findall(r'http://[a-z-./]+', line.decode().strip())[0])
    
html = '<p>See <a href="https://example.com/page">this page</a> and <a href="https://example.org/other">another</a>.</p>'
pos = html.find('href="')
pos


from bs4 import BeautifulSoup

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


url = input("Enter Your URL: ")
html = urllib.request.urlopen(url).read()
print(html)
soup = BeautifulSoup(html, 'html.parser')
print(soup)
# Retrieve all of the anchor tags
tags = soup('a')
print(tags)
for tag in tags:
  print(tag.get('href', None))

re.findall(r'http://.*', '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>')

# practice py4e_1
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


url = input("Enter Your URL: ")
html = urllib.request.urlopen(url).read()
#print(html)
soup = BeautifulSoup(html, 'html.parser')
#print(soup)
spans = soup('span')
# print(spans)
outcome = 0
for span in spans:
  number = span.contents[0]
  number = int(number)
  outcome += number
  
print(outcome)

# practice py4e_1
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


url = input("Enter Your URL: ")
count = int(input("Enter the number of time you want to click links: "))
position = int(input("Enter the position that you want to reach at each link to get the final name: "))
num = 0
while num < count:
  html = urllib.request.urlopen(url).read()
  # print(html)
  soup = BeautifulSoup(html, 'html.parser')
  #print(soup)
  names = soup('a')
  #print(names)

  url = names[position-1].get('href', None)
  num +=1
    
print(names[position-1].contents[0])
  