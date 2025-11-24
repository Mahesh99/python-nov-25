s="python"
s2='python'
s3="""python"""
s4='''python'''

s5="""This is
a multiline
string"""
print(s5)

s6="python" "programming"
s6="python" \
    "programming"
print("python" "programming")

s7=s+s4+\
    s2+s3



#what if our text has single or double quotes in it

quotation = "\"Knowledge is power\""
print(quotation)


#what if our text has single or double quotes in it

quotation = '"Knowledge is power"'
print(quotation)

"""
Escape sequences
\" - double quote
\' - single quote
\\ - backslash

\n - newline
\t - tab
\r - carriage return
\a - alert (bell)
\b - backspace
"""

print("\tHello\nWorld")
print("hello\bworld")
print("programming\rworld")

# Indexing
s="python"
# p  y  t  h  o  n
# 0  1  2  3  4  5
#-6 -5 -4 -3 -2 -1
print(s[0])
print(s[5])
print(s[-6])
print(s[-1])

s2="hello world"
print(s2[5])
print(s2[6])

# len() function
# returns the length of the string

s="python"
print(len(s))
print(len("hello world"))
print(len(""))
print(len(s2))
k=len("python basics")
print(k)

# slicing
s="python programming"
# p  y  t  h  o  n     p  r  o  g  r  a  m  m  i  n  g
# 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17
#-18-17-16-15-14-13-12-11-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
# start index : end index (end index not included)

print(s[0:6])
print(s[4:10])

# you can omit start index or end index
print(s[:6])
print(s[7:])
print(s[:])
print(s)
a=s[:6]
b=s[7:]
print(a)
print(b)

# step in slicing
# syntax: string_name[start_index:end_index:step]
s="python programming"
s1=s[0:6:2]
print(s1)

# string methods
# upper(), lower(), title(), count(), find(), replace(), strip(), split(), join()

s="Python programminG"
s2=s.upper()
print(s2)

s3=s.lower()
print(s3)

s4=s.title()
print(s4)

s5=s.replace("o", "0")
print(s5)

s6=s.replace("Python", "java")
print(s6)

s7="  hello       world  "
s8=s7.strip()
print(s8)

s9="hello world program world"
count_w=s9.count("world")
print(count_w)

index_w=s9.find("world")
print(index_w)



# split & join
s = "hello world welcome to python"
words = s.split()  # default separator is space
print(words)

# split with a specific separator
s2 = "apple,banana,cherry,dates"
fruits = s2.split(",")
print(fruits)

# join
# words=['hello', 'world', 'welcome', 'to', 'python']
# s2 = "*".join(words)
s2 = " ".join(words)
print(s2)

# index()
s9="hello world program world"
# idx = s9.index("world") # 6
# idx = s9.index("wold") # ValueError
idx = s9.find("pro")
print(idx)

# isalpha(), isdigit(), isspace(),isalnum()
s10="hello"
s11="hello123"
s12="   "
print(s10.isalpha())  # True
print(s11.isalpha())  # False
print(s12.isspace())  # True    
print(s11.isdigit())  # False
s13="12345"
print(s13.isdigit())  # True
print(s11.isalnum())  # True
print(s10.isalnum())  # True
s14="hello123 "
print(s14.isalnum())  # False

