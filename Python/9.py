a= int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Swap with temporary number
temp = a
a = b
b = temp


print(f"After swapping: First number = {a}, Second number = {b}")


a = int(input("Enter the first number and input: "))
b = int(input("Enter the second number: "))

# Swap without using a temporary number
a = a + b  
b = a - b  
a = a - b  


print(f"After swapping: First number = {a}, Second number = {b}")
