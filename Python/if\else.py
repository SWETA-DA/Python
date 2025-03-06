a=int(input("enter A:"))
b=int(input("enter B:"))
c=int(input("enter B:"))
if a>b:
    if a>c:
        print(a,"is max")
    else:
        print(b,"is max")
elif b>c:
    print(b,"is max")
else:
    print(c,"is max")
