# Operations on tuple

tup1 = ("INDIA,AUSTRELIA,ENGLAND,AMERICA,RUSSIA,")
tup2 = ("PAKISTAN,SHRELANKA,CHINA,AFGANISTAN")

combine = tup1 + tup2 ,("all are one")   # we can add two tuples and convert into another as like list
print(combine)


print(tup1.count("INDIA")) # this operation provides the count of element in the tuple

p = (12,23,34,45,56,67,78,89,90,12,23,34,34,45,56,687,79,9)
print(type(p))

print(p.index(34)) # this operation retuns the first acurance of the from the given element from tuple
print(p.count(34))

print(p.index(34,0,len(p)-1)) # in this conditon - 34 is the value ,0 is the initial and len(p)-1 is the final , through this way we can find the amount of occorance
print(len(p))


# countries = ("INDIA,AUSTRELIA,ENGLAND,AMERICA,RUSSIA")

# temp = list(countries)
# temp.append("ierland")
# temp.pop(3)
# print(countries)

s = (23,45,56,34)
print(s)
print(type(s))
# s[2] = 23 # cannot do this