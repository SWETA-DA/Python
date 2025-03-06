def split_list_into_variables(input_list):
    
    if len(input_list) < 3:
        print("The list must have at least 3 elements.")
        return
    
 
    var1, var2, var3 = input_list[0], input_list[1], input_list[2]
    
   
    print(f"var1 = {var1}")
    print(f"var2 = {var2}")
    print(f"var3 = {var3}")


input_list = [10, 20, 30]  
split_list_into_variables(input_list)
