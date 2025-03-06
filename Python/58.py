from collections import Counter


list_of_dicts = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}
]


counter = Counter()

for d in list_of_dicts:
    counter[d['item']] += d['amount']
print("Combined values:", counter)
