
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))


if a == b or b == c or a == c:
    print("The sum is 0 because two values are equal.")
else:
    total = a + b + c
    print(f"The sum of the three integers is: {total}")
