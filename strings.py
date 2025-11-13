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
\"
\'
\\
\n
\t
\r
\a
\b
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

# slicing
s="python programming"
# p  y  t  h  o  n     p  r  o  g  r  a  m  m  i  n  g
# 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
#-17-16-15-14-13-12-11-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
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

