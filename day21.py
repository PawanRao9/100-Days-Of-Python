# # # # # FUNCTION ARGUMENT......

# # # def average(a,b):
# # #     print("the average will be:", (a+b)/2)
# # # average(3,6)


# # # # the function argumentas are of four types-
# # # # 1 - default argumrnt
# # # # 2 - keyword argument
# # # # 3 - variable length argument
# # # # 4 - required argument


  
# # default argument -
# def average(a=2,b=4):
#     print("the average will be:", (a+b)/2)
# average(3,6)
# average()    # if you don't provide any agumnts then by defaultly the arguments will be 2 and 4 for this condition, the values are known as the default values
# average(a=4) 
# average(b=2) # if you want to change the value of the b or a then the values can be changd


# # # keyword arguments -
# # def average(a=2,b=4):
# #     print("the average will be:", (a+b)/2)

# # average(b=12,a=13) # this way the python interpriter will recogonise the arguments by the parameters name ,hence the order doesn't matters


# # # # Required arguments -
# # # def average(a,b=4):  # the arguments are need to be passed for every parameter ,and the number of arguments are shuld match with the function defination
# # #     print("the average will be:", (a+b)/2)
# # # average(b=123)     


# variable length argument -

def average(*numbers):
    sum = 0
    for i in numbers:
     sum = sum +i
     print("the average will be :",sum/ len(numbers))
average(3,6)        



