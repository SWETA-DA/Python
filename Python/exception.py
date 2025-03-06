print("Start Code")

try:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b
    print("Division:",c)
    l=["java","paython","php","testing"]
    index=int(input("Enter index number :"))
    print(l[index])
except ZeroDivisionError as e:
    print("Exception Caught :",e)
except ValueError as e:
    print("Exception Caught :",e)
except IndentationError as e:
    print("Exception Caught :",e)
print("End Code")