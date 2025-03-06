'''
for i in range(65,73):
    print(" "*(73-i),end="")
    for j in range(65,i):
        print(chr(j),end=" ")
    print()

n=int(input("enter ASCI code for Alphabate Patten(65-90)"))
for i in range(n,n+9):
    print(" "*((n+9)-i),end="")
    for j in range(n,i):
        print(chr(j),end=" ")
    print()

n=int(input("enter ASCI code for Alphabate Patten(65-90)"))
for i in range(n,91):
    print(" "*(91-i),end="")
    for j in range(n,i):
        print(chr(j),end=" ")
    print()
'''
for i in range(65,73):
    print(" "*(73-i),end="")
    for j in range(65,i):
        print(chr(j),end=" ")
    print()
