# LIST METHODS...

list = [12,32,45,56,67,78,89,90,1,56,3,77]
print(list)

list.append(21) # this method is used for adding any aditional deta in the list at the end
print(list)
print(len(list))

list.sort() # this method is used for sorting the list
print(list)

list.sort(reverse=True) # this method is used for sorting the list in the reverse order
print(list)

list.reverse() # this method is used for reversing the list
print(list)

print(list.index(56)) # this method is used for printing the index value
print(list)

print(list.count(56)) # this method is used for counting the count of any value

list.insert(2,"pawan") # this method is used for inserting any deta at any index as per required
print(list)

m = ["ducati","lamborgini","land rover","pagani","bmw"]
list.extend(m) # this mentod will connect both the lists as one list
print(list)

k = list + m # this mentod will connect both the lists as one list
print(k)

s = list.copy() # this method will copy the list in the s and you can chage anything or add anything and that wont be change the main list;
s[0] = 2
print(s)
print(list)

l = []
print(l)
l.append(23)
print(l)    