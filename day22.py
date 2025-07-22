# LIST.....

manga = [12,10,1,44,23,]
print(manga)
print(type(manga))

# the lists are the ordered collection of the data
# the list can store multiple items in a single variable
# lists are muteable, which means the values of the list can be change

# print(manga[0]) # []-are used to call a list
# print(manga[1])
# print(manga[2])
# print(manga[3])
# print(manga[4])
# print(manga[5])

# print(len(manga))


print(manga[-4]) # negetive indexing....
print(manga[-3])
print(manga[-2])
print(manga[-1])

# print(manga[len(manga)-3]) # positive index

# a = int(input("enter a number:")) # same thing applies for string as well
# if a in manga:
#     print("hai bhai isme")
# else:
#     print('nai hai')    

print(manga)
print(manga[1:len(manga)-1:2]) # the way is known as the JUMP INDEXING ,by which you can skip the alteration as per required


# LIST COMPREHINSION..

list =[i for i in range(20)]
print(list)
list = [i*i for i in range(20) if i%2==0]
print(list)
print(list[1:len(list)-1:2])