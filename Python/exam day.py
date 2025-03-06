'''
n=int(input("enter n:"))


for i in range(4,10):
    for j in range(0,i):
        print(i,end=" ")
    print()

n=int(input("enter n:"))
for i in range(n,n-7,-1):
    for j in range(i,n):
        print(i,end=" ")
    print()

a=int(input("enter n that is prime number:"))
if a%2!=0:
    for i in range(3,int(a/2)+1,2):
        if a%i==0:
            print(a,"is not prime")
            break
    else:
        print(a,"is prime")
else:
    print(a,"is not prime")
'''
for i in range(9,3,-1):
    for j in range(i,10):
        print(i,end=" ")
    print()
