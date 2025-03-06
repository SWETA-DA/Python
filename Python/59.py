input_string = "hello world"

letter_count = {}

for char in input_string:
    if char != ' ':
       
        if char in letter_count:
            letter_count[char] += 1

        else:
            letter_count[char] = 1

print("Letter count:", letter_count)
