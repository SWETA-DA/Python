def get_unique_values(input_list):
    return list(set(input_list))
input_list = [1, 2, 2, 3, 4, 4, 5, 1, 6]
unique_values = get_unique_values(input_list)
print(f"Unique values from the list: {unique_values}")
