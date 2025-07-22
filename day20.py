# FUNCTIONS

def calculategmean(a, b):                     #function deffination
    gmean = (a*b)/(a+b)
    print("the mean will be: ",gmean)

def isgreter(a,  b):                           #function deffination
    if(a>b):
        print("the first is greater")
    else:
        print("secound is greater")    
def isleser(a,b):                               #function deffination
    if(a<b):
        print("the first is leser")
    else:
        print("secound is leser") 


a =int(input("enter the first value: "))
b =int(input("enter the second value: "))
calculategmean(a, b)                           #function call
isgreter(a, b)                                 #function call
isleser(a, b)                                  #function call

c =int(input("enter the first value: "))
d =int(input("enter the second value: "))
calculategmean(c, d)                           #function call
isgreter(c, d)                                 #function call
isleser(c, d)  



# function is block of codes that works multiple time as we pass the arguments in it
# it is of two types "builtin functions","user define functions"
# 
# builtin fun - these are the type of functions that are made by the user
# userdefine fun - the are the type of functions that are made by user as per requirement


def isequal(a,b):
    pass               # the pass actually describes that the logic or code will be writen later     



