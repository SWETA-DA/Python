my_dict = {'a': 50, 'b': 100, 'c': 200, 'd': 300, 'e': 250}


top_3 = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)[:3]
print("The top 3 highest values are:")
for key, value in top_3:
    print(f"{key}: {value}")
