#0 1 1 2 3 5 8 -> Fibonacci Series

n=int(input("enter N: "))
a,b=0,1
print(a,end="")
while b<n:
    print(b,end="  ")
    a,b=b,a+b
