def read_first_n_lines(file_name, n):
    try:
        
        with open(file_name, 'r') as file:
        
            for i in range(n):
                line = file.readline()
                if line:  
                    print(line.strip())  
                else:
                    print(f"End of file reached after {i} lines.")
                    break
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")


file_name = 'example.txt'  
n = 5  

read_first_n_lines(file_name, n)
