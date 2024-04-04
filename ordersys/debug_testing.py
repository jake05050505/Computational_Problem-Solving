from collections import OrderedDict
unsorted = {3:'test3',0:'test0',2:'test2'}
print(f'unsorted: {unsorted}')
sorted = OrderedDict(sorted(unsorted.items()))
print(f'sorted {sorted}')