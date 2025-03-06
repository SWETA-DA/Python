def get_first_and_last_two_chars(string):
    
    if len(string) < 2:
        return ""  
    else:
        
        return string[:2] + string[-2:]
input_string = input("Enter a string: ")
result = get_first_and_last_two_chars(input_string)
print(f"Result: {result}")
