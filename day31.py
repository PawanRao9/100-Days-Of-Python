# SET........
s ={12,34,34,45.67,56,67,78,89,56,67}
print(s)
print(type(s))


# sets are the 'unordered' collecction of deta items ,they store multiple types of data items ,and the items are enclosed with in {};

info = {"ola","2",3,56,3,56,5,True,"$"}
print(info)
print(type(info))


# sets doesn't allow duplicate value

harry = {" "}
print(type(harry))

happy = set()
print(happy,type(happy))

for values in info:
    print(values)


a = {12,23,34,12}
b = {67,78,89,12}

result = a.union(b)
result1 = a.intersection(b)
print(result,result1)


