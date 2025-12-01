"""
7
2 to 6

n=15

2 to 14(n-1)

n%2==0
when break is executed inside a loop current iteration and all next iteration will be terminated.
And code after the loop will be executed
"""
# Prime number check
# n=int(input("Enter a number: "))
# prime=True
# for i in range(2,n//2+1):
#     if n%i==0:
#         prime=False
#         break
# if prime:
#     print("Number is Prime")
# else:
#     print("Number is not Prime")




# Factorial of a number
# n=int(input("Enter a number: "))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(f"Factorial of {n} is {fact}")
"""
fact=1
for i in range(1,n+1):
    fact*=i

Iteration 1: fact=1 i=1 
    fact*=i=> fact=1*1=1

Iteration 2: fact=1 i=2
    fact*=i=> fact=1*2=2

Iteration 3: fact=2 i=3
    fact*=i=> fact=2*3=6

Iteration 4: fact=6 i=4
    fact*=i=> fact=6*4=24

Iteration 5: fact=24 i=5
    fact*=i=> fact=24*5=120
"""



# rollnos=["13311A1247","13311A1248","13311A1249","13311A1250"]
# new_rollnos=[]
# for no in rollnos:
#     nr = no[-2:]
#     new_rollnos.append(int(nr))
# print(new_rollnos)



# for no in range(1,10):
#     print(int(no))
#     break
# else:
#     print("Loop completed successfully")



# star pattern -1
# *
# **
# ***
# ****
# *****
# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     print("*"*i)


# star pattern-2
#     * i=1
#    * *
#   * * * 
#  * * * * 
# * * * * *


# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     print(" "*(n-i)+"* "*i)



# number pattern-1
# for i in range(1,n+1):
#     print(f"{i} "*i) # "3"*3


# number pattern-2
# n=int(input("Enter a number: "))
# c=1
# for i in range(1,n+1):
#     for j in range(i):
#         print(c,end=" ")
#         c+=1
#     print()


# number pattern-3
# n=int(input("Enter a num:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


# Find the greatest number among two numbers
# a=int(input("Enter first num:"))
# b=int(input("Enter second num:"))
# if a>b:
#     print(f"{a} is greater")
# else:
#     print(f"{b} is greater")


# sum of digits of a number
num=int(input("Enter a number:")) # 123
sum=0
while num>0:
    digit=num%10
    sum+=digit
    num=num//10
print(f"Sum of digits is {sum}")


"""

iteration:1 => num=123,sum=0
while 123>0: => True
    digit=num%10 = 123%10 => 3
    sum+=digit => 0+3
    num=num//10 = 123//10 => 12

iteration: 2 => num=? sum=?
"""