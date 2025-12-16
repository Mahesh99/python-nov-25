# 0 1 1 2 3 5 8 13 21 34 55 89 ...

first_ten=[0,1,1,2,3,5,8,13,21,34]

# prints n elements of fibonacci series
def fib(n):
    count=0
    a=0
    b=1
    while count<n:
        print(a)
        c=a+b
        a=b
        b=c
        count+=1

def fib2(n):
    result=[]
    a=0
    b=1
    for _ in range(n):
        result.append(a)
        a,b=b,a+b
    return result



if __name__=="__main__":
    fib(7)
    print(fib2(8))