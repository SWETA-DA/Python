'''

n=int(input("enter n:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

n=int(input("enter n:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()


n=int(input("enter n:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    print()
'''
n=int(input("enter n:"))
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(i,0,-1):
        print(j,end=" ")
    print()



