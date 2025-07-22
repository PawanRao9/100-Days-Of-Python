# costum errors...

# a = int(input("Enter a num in between 12 and 20 to enter  :"))

# if (a<12 or a>20):
#     raise ValueError("the value shuld be in between the 12 and 20 !")
# else a== quit:
#     print ("you may enter ")

# '''python has inbuild errors apart from that we can rasie costum errors to stop the program
# and to not procede further !
# '''    

# class A :
#     def sun_of(self):
#       print("father is the sun of two childs")
# class B(A):
#     def father_of(self):
#       print("b is the first sun of a")

# a = a()
# a.sun_of()



a = input("enter some values :")

if a == "quit":
    print("you are quitting now!")
    exit()

try :
    a = int(a)
    print(a)
    
    if a > 10 or a < 20 :
        raise ValueError("the error occoured !")
    else:
        print("ok")
except ValueError:
    print("invalid input,please correct it !")

# finally :
#     print("this is the code")    
