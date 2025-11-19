"""
Output:
Enter words: python java hello list tuple zero
The last word in the dictionary is zero
"""
inp=input("Enter words:") # "python java hello list tuple zero"
words=inp.split() # ['python', 'java', 'hello', 'list', 'tuple', 'zero']
last_w=max(words) # 'zero'
print("The last word in the dictionary is "+last_w)