
string = input("Enter a string: ")

if len(string) >= 3:
   
    if string.endswith("ing"):
        string += "ly"
    else:
       
        string += "in"
print(f"Modified string: {string}")
