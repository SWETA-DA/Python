
file_name = 'example.txt'  


text_to_append = "\nThis is the appended text."


with open(file_name, 'a') as file:
    file.write(text_to_append)


with open(file_name, 'r') as file:
    content = file.read()
print("Updated file content:")
print(content)
