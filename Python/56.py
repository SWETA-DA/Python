from collections import Counter


keys = ['a', 'b', 'c']
values = [400, 400, 300]


mapped_dict = dict(zip(keys, values))


counter_dict = Counter(mapped_dict)
print(counter_dict)
