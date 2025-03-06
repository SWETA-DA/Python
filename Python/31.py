def count_strings_with_same_first_and_last(lst):
    count = 0
    for string in lst:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count

# 
strings_list = input("Enter a list of strings (separated by spaces): ").split()
result = count_strings_with_same_first_and_last(strings_list)
print(f"Count of strings where the first and last characters are the same: {result}")
