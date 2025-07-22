# SET METHODS


s1 = {1,2,3,4,5}
s2 = {1,3,5,7,9}

s3 = s1.union(s2) # this way we can run union function in between two or more sets
s4 = s1.intersection(s2) # this way we can run intersection function in between two or more sets
print("the union is: ",s3,"\n","the intersection is: ",s4)

print("one element is poped :",s1.pop()) # this method is used for poping the last element from the set , the poping will always from the end
print("one element is poped :",s1.pop())
print("one element is poped :",s1.pop())
print("one element is poped :",s1.pop())
s1.update(s2)
print(s1, s2)

s6 = s1.symmetric_difference(s2) # the symetric diffence refers to (a-b)U(b-a)
print(s6)

print(s1.remove(5))




p = {12,34,56,78,67}
q = {12,34,67,89,45}
r = p.symmetric_difference(q)
print(r)

print(p.difference(q))
print(p.intersection_update(q))
print(p.update(q))






a = {"africa","malesia","mongolia","minemar"}
b = {"india","ameraca","minemar","mongolia"}

print(a.union(b))
print(a.isdisjoint(b)) # this method checks if the elements of one set is present in the other set if yes then it will return "false",else it will return "Ture" 


king = {12,23,34,56,67,89,58}
butler = {12,34,89}

result = king.issuperset(butler) # this method will show if the set is super-set of another or not
result1 = butler.issubset(king) # this method will show if the set is sub-set of another or not
result2 = king.issubset(king)
print(result, result1, result2)








king.add(69) # this method will add the  only one element in the set at a random place
print(king)

katapa = (555,666,777,888)

king.update(katapa) #this method will add more items in the main set
print(king)

king.remove(555) #this method will remove the element that we want from the set
print(king)

# del king   # del is a key word as it will delete the set then the erroe wil be spon 
# print(king)

# king.clear() # it will delete only all the elemeys in the set not the set
# print(king)


info = {666,777} # through this method we can check if a elements is present in the set or not
if 666 in info:
    print("present")
else:                 
    print("not present")




      