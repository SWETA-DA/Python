def remove_duplicates(input_list):
    
    return list(set(input_list))
input_list = [1, 2, 3, 4, 5, 2, 3, 6, 7, 1]
result = remove_duplicates(input_list)
print(f"List after removing duplicates: {result}")
