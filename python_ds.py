fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line1 = line.rstrip()
    num1 = line1.find(":")
    output = line1[num1+1:].lstrip()
    total = total + float(output)
    count = count + 1
result = total/count
    
print(f"Average spam confidence: {result}")


"X-DSPAM-Confidence:    0.8475".find(":")

fruit = "Banana"
fruit[0] = "b"
print(fruit)

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(len(c))

friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
friends

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    for word in line.rstrip().split():
        if word in lst: continue
        lst.append(word)
lst.sort()
print(lst)


fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "my_file.txt"

fh = open(fname)
count = 0
for line in fh:
    if line.startswith("From "):
        my_list = line.rstrip().split()
        print(my_list[1])
        count = count + 1
print("There were", count, "lines in the fle with From as the first word")
        
stuff = dict()
print(stuff['candy'])

stuff = dict()
print(stuff.get('candy',-1))

name = input("Enter file:")
if len(name) < 1:
    name = "my_file.txt"
handle = open(name)
my_dict = dict()
for line in handle:
    if line.startswith("From "):
        item_list = line.strip().lower()
        item_list = item_list.split()
        my_dict[item_list[1]] = my_dict.get(item_list[1], 0) + 1

number_max = None
person_name = None 
for person, num_msg in my_dict.items():
    if person_name is None or number_max < num_msg:
        person_name = person
        number_max = num_msg
        
print(person_name, number_max)
 
 
handle = open('my_file.txt')
my_dict = dict()
for line in handle:
    if line.startswith("From "):
        item_list = line.strip().lower()
        item_list = item_list.split()
        #print(item_list[1])
        my_dict[item_list[1]] = my_dict.get(item_list[1], 0) + 1
        print(my_dict)
        

a = (9, 2,4,5,1)
a[2]
b = [3,6,7,2,1]
sorted(b)

A= "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008".split()
len(A)
name = input("Enter file:")
if len(name) < 1:
    name = "my_file.txt"
handle = open(name)
dict1 = {}
for line in handle:
    if line.lower().startswith("from "):
        my_time = line.split()[5]
        hr = my_time.split(":")[0]
        dict1[hr] = dict1.get(hr, 0) + 1
        
for yr, num in sorted([(key, value) for key, value in dict1.items()]):
    print(yr, num)