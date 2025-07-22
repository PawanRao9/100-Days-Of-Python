#DICTIONARY METHODS...........

#update() - this method will update one dict with another dict

ep1 = { 123:34,133:24,134:23,234:13}
ep2 = {12:24,245:13,132:24}

ep1.update(ep2)

print(ep1)
print(len(ep1))

# clear() - This method basically used for printing the empty string or to clear any dictionary

# ep1.clear()
# print(ep1)
# empt = {}
# print(empt) 

#pop() - this method is used for poping a key value pairs from the dict

# ep1.pop(12) # erroe hai bhai !
print(ep1)

ep3 = ep1.popitem()
del ep1[123]
print(ep3)