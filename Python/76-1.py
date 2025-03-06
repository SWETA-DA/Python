
def read_file_into_list(file_name):
    try:
        with open(file_name, 'r') as file:
           
            lines = file.readlines()
            
    
        lines = [line.strip() for line in lines]
        
        return lines
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


file_name = 'example.txt' 
lines_list = read_file_into_list(file_name)

print("Lines from the file:")
for line in lines_list:
    print(line)
