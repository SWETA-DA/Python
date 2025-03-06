def check_empty_list(input_list):
    
    if not input_list:
        return "The list is empty."
    else:
        return "The list is not empty."

input_list = []  
result = check_empty_list(input_list)
print(result)
