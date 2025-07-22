# TUPLE......
T = (1,4,6,7,8,9,7,6,7,True,"santra") #we use () for defining a tuple , and the items are separated by using comma - "," , tuples are unchangeable which mans we cannot change/alter the items after creation
print((T),type(T))
            
 
           # TUPPLES ARE IMMUTABLE


P = (2,)          # in this condition we have to add a comma at the end, else it will print the value as a intiger .
print((P),type(P)) 

print(T[0]) # through this way we can print the items in a tupple as per index value
print(T[1])
print(T[2])
print(T[3])
print(T[4])
print(T[5])

print(T[-5]) # Negetive indexing
print(T[-4])
print(T[-3])
print(T[-2])
print(T[-1])
print(T[len(T)-1])


print(len(T))

# a = str(input("enter a string : "))
# a1 = int(input("enter a number : "))
# if a in T:
#     print("present")
# else:
#     ("not presrent")    

# if a and a1 in T:
#     print("hai bhai")   # YE PEHLE KR 
#     if a in T:
#         print("bas yehi hai")
#     elif a1 in T:
#         print("Baas yehi hai")    
# else:
#     print("nai hai")  

T1 = T[0:4]
print(T1)

print(T.count(7))