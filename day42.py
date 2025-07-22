# R=ENUMERATE FUNCTION ..........

marks = [12,334,231,244,12,1,232,4,24,]

''' the 'ENUMERATE' is the function in python that allows you to loop over a sequence
(such as list ,touple,or srings) and get the index and value of each element in the sequence at hte same time'''

# index = 0
for index,mark in enumerate(marks,start =1) :  
    print(mark)
    if index == 3:
        print("wassup!")
    # index += 1    
    # else :
    #     print("null")


fruits = ["apple","banana","pineapple","orrange"] 

for index, fruit in enumerate(fruits):  # this is the easiest way for the for loop
     print(fruit,index)