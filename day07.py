#OPERATORS -
a = 8
b = 20
print(a+b)#adition
print(a-b)#substraction
print(a*b)#multiplication
print(a%b)#division
print(a==b)#equals to
# print(a=b)#assingment - error
print(b**a)#exponentional



# ---------CALCULATOR-------------
 
a = int(input("enter First no :"))
b = int(input("enter Secound no :"))

print("\n--PAWANS SASTA CALCULATOR--") 
print("1=addition\n2=substration\n3=multiplication\n4=division")
c =int(input("enter your choice :"))
if c == 1 :
    print("adition operation:",a+b)
elif c == 2 :
    print("substration operation :",a-b)
elif c == 3 :
    print("multiplication :",a*b)
elif c == 4 :
    print("division :",a/b)
else :
    print("enter valid option")


print("end")       

#----------------------------------
          