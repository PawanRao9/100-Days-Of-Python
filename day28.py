# F-STRINGS....


'''With .format(), you use curly braces {} as place holders within a string.
 The values passed into the format() method are inserted into these place holders in order.'''

my = "shut the {0} and come {1}"
d = "dore"
i = "in"


print(my.format(d, i)) # format is the type of the function in the string format
print(my.format(d, i))


print(f"knoch the {d} and come {i}") # we can do even like this to reduce the code

print(f"{2 * 23}") # we can do even like this
