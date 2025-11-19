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
