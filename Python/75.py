
def read_last_n_lines(file_name, n):
    try:
        with open(file_name, 'r') as file:
         
            lines = file.readlines()
            
          
            last_n_lines = lines[-n:]
            
          
            for line in last_n_lines:
                print(line.strip())
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_name = 'example.txt'  
n = 5  

read_last_n_lines(file_name, n)
