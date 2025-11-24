# Data types
# string, int, float, bool
# list, tuple, set, dict

# list
# creating a list
my_list = [1, 2, 3, 4, 5]
my_list2 = ["apple", "banana", "cherry"]
my_list3 = [1, "apple", 3.14, True]
print(my_list)

# accessing elements
print(my_list[0])  # first element
print(my_list2[1]) # second element

# modifying elements
my_list2[2] = "orange"
print(my_list2)

print(my_list3[1])
my_list3[2]=10
print(my_list3)

print(my_list2[2])


# slicing
# slicing syntax: list_name[start_index:end_index]
# end_index is not included
my_list = [10, 20, 30, 40, 50, 60, 70]
list2= my_list[2:5]
print(list2)

print(my_list[4:])

print(my_list[0:3])
print(my_list[:3])

# step in slicing
# syntax: list_name[start_index:end_index:step]
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
l3= my_list[1:8:2]
print(l3)

l4= my_list[0:8:2]
print(l4)


l5= my_list[::2]
print(l5)

l6= my_list[0:8:3]
print(l6)

# reversing a list using slicing
l7= my_list[::-1]
print(l7)

# list methods
# append(), extend(), insert(), remove(), pop(), clear(), index(), count(), sort(), reverse()

# list method syntax: list_name.method_name(arguments)

my_list = [5, 2, 9, 1, 5, 6]
my_list.append(3)
print(my_list)
my_list.append(10)
print(my_list)

my_list.remove(5)
print(my_list)
# my_list.remove(100)  # will raise ValueError as 100 is not in the list
p=my_list.pop()  # removes last element
print(my_list)
print(p)
my_list.pop(2)  # removes element at index 2
print(my_list)

my_list.sort(reverse=True)
print(my_list)

my_list.reverse()
print(my_list)

my_list.insert(2, 15)  # insert 15 at index 2
print(my_list)

# extend
my_list2 = [20, 25, 30]
my_list.extend(my_list2)
print(my_list)

# index
idx = my_list.index(15)
print(idx)

# idx2 = my_list.index(50)
# print(idx2)

# count
my_list.append(5)
cnt = my_list.count(5)
print(cnt)

# nested list
my_list.append(my_list2)
# clear
my_list.clear()
print(my_list)

# list functions
# len(), min(), max(), sum()
my_list = [5, 2, 9, 1, 5, 6]
print(len(my_list))
print(min(my_list))
print(max(my_list))
print(sum(my_list))
print(sum(my_list)/len(my_list))  # average

# split & join
s = "hello world welcome to python"
words = s.split()  # default separator is space
print(words)

# join
# words=['hello', 'world', 'welcome', 'to', 'python']
# s2 = "*".join(words)
s2 = " ".join(words)
print(s2)

# tuple
# creating a tuple
my_tuple = (1, 2, 3, 4, 5)
my_tuple2 = ("apple", "banana", "cherry")
my_tuple3 = 1, "apple", 3.14, True
print(type(my_tuple3))
# print(sum(my_tuple))
print(min(my_tuple2))
print(max(my_tuple2))

# dir()
print(dir(my_tuple))
print(dir(list))


# Set
# creating a set
my_set = {1, 2, 3, 4, 5,1,2,3}
my_set2 = {"apple", "banana", "cherry","apple"}
my_set3 = {1, "apple", 3.14, True}
print(my_set)
print(my_set2)

# accessing elements
# sets are unordered, so we cannot access elements by index

# modifying elements
my_set.add(6)
print(my_set)
my_set.remove(3)
print(my_set)

# list(), set(), tuple() conversions
fav_actors = ["Prabhas","Shruthi Haasan","Naani","Ram Charan","Prabhas","Nivedha Thomas","Naani",
                   "Ram Charan","Rakul Preeth","Samantha","Rakul Preeth","Prabhas","Samantha",
                  "Nivedha Thomas","Naaga chaithanya","Salman khan","Salman khan","Vijay","Shradha kapoor","Vijay",
                  "Shruthi Haasan","Naani","Ram Charan","Prabhas","Nivedha Thomas","Naaga chaithanya","Salman khan"]
print(len(fav_actors))

unique_actors = set(fav_actors)
print(len(unique_actors))
print(unique_actors)

fav_actors2 = list(unique_actors)
fav_actors2.sort()
print(fav_actors2)

fav_actors2=list(set(fav_actors))
fav_actors2.sort()
print(fav_actors2)  

print(dir(set))

set_a={1,2,3,4,5}
set_b={4,5,6,7,8}
# union
set_c= set_a.union(set_b)
print(set_c)

# intersection
set_d= set_a.intersection(set_b)
print(set_d)

# issubset
set_e={1,2}
print(set_e.issubset(set_a))
print(set_a.issubset(set_e))

# pop()
set_n= {30,40,10,20,60}
elem= set_n.pop()
print(elem)
print(set_n)

print(help(set.pop))


# Dictionary
# creating a dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict)

# accessing elements
print(my_dict["name"])

# modifying elements
my_dict["age"] = 31
print(my_dict)

my_dict["country"] = "USA"  # adding new key-value pair
print(my_dict)

# dictionary methods
# keys(), values(), items(), get(), pop(), popitem(), clear(), update()

print(my_dict.keys())
print(list(my_dict.keys()))
print(my_dict.values())
print(my_dict.items())

# get()
print(my_dict.get("name"))
print(my_dict.get("salary"))  # returns None if key not found
print(my_dict.get("salary", 50000))  # returns 50000 if key not found
print(my_dict.get("age", 25))  # returns 31 as age key is present

# pop()
age = my_dict.pop("age")
print(age)
print(my_dict)

# popitem()
item = my_dict.popitem()
print(item)
print(my_dict)

# update()
my_dict.update({"age": 32, "city": "Los Angeles"})
print(my_dict)

# clear()
my_dict.clear()
print(my_dict)

s=""
l=[]
t=()
st=set()
d={}

# Membership operators: in, not in
s="hello world"
print('h' in s)
print('z' not in s)
print('z' in s)

# list
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)
print(6 not in my_list)
print(6 in my_list)

# in, not in applicable same as list for tuple, set

# Dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}
print("name" in my_dict)  # checks for key
print("salary" not in my_dict)
print("John" in my_dict)  # checks for key, not value

# Identity operators: is, is not
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)  # True, as b references same object as a
print(a is c)  # False, as c is a different object with same content

s="hello"
s1="hello"
print(s is s1)  # True, as both refer to same string object in memory

# nested data structures
my_list= [1, 2, [3, 4], (5, 6), {"name": "John"}]
print(my_list[2])  # [3,4]
print(my_list[2][0])  # 3

my_dict = {"name": "John", "age": 30, "address": {"city": "New York", "zip": "10001"}}
print(my_dict['age'])  # 30
print(my_dict["address"]["city"])  # New York
