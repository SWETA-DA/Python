
file_name = 'example.txt'  

try:
    with open(file_name, 'r') as file:
       
        content = file.read()
        
      
        print(content)
except FileNotFoundError:
    print(f"The file '{file_name}' was not found.")
