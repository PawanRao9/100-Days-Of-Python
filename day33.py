# DICTIONARY ...........


# dictionaries are the ordered collection of data items , they store multiple items in a single variable , dicts are the key value pairs they separeted by the commas , and enclosed withmin curly brackets

dict = {"name":"pawan","class":"BTech","reg no":2301348187,"sec":"b"} 
print(dict)
print(type(dict))
print(dict["name"])



secoundyear = {
    
    2301348187 : "pawan",
    2301348007 : "barsha",
    2301348138 : "mj",
    2301348257 : "suman",
    2301348137 : "monali",
    2301348169 : "priyanshu",
    2301348156 : "pragnya",

}         # in this condition we can say that the numbers are the key values and the names are the calues

print(secoundyear[2301348187])
print(secoundyear[2301348007])
print(secoundyear.keys())
print(secoundyear.values()) 
print(secoundyear)
# print(secoundyear{key})

for keys in secoundyear:
    print(keys)
    print(f"the values corresponding to the {keys} is :{secoundyear[keys]}")    


print(secoundyear.items())





