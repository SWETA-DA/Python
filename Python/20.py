str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")


if len(str1) >= 2 and len(str2) >= 2:
    swapped_str1 = str2[:2] + str1[2:]
    swapped_str2 = str1[:2] + str2[2:]
else:
    swapped_str1 = str2 + str1
    swapped_str2 = str1 + str2


result = swapped_str1 + " " + swapped_str2

print(f"Result after swapping: {result}")
