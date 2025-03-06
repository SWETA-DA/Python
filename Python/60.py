input_string = 'w3resource'


char_count = {}


for char in input_string:
    
    if char in char_count:
        char_count[char] += 1
    
    else:
        char_count[char] = 1
print(char_count)
