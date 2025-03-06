import random

def select_random_item(item_list):
    return random.choice(item_list)
items = [1, 2, 3, 4, 5, "apple", "banana", "cherry"]
random_item = select_random_item(items)
print(f"Randomly selected item: {random_item}")
