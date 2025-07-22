# using of the FIANLLY keyword....

# while(True):
#   try :
#     a = int(input("enter a num :"))
#     b = int(input("enter b num :"))

#     c = a+b / 2

#     print(c)
#   except Exception as e:
#     print(f"An Excepyion Occoured !")
#   finally:
#     print("Do Not Deal With The Error Handeling")    

def fum():
    try :
        a = [12,34,5,45] 
        i = int(input('enter a num :'))
        print(a[i])
        return 1
    except :
        print("one exception occoured !")
        return 0
    finally:
       print("this line will be printed")    

s = fum()
print(s)


# * you cannt use the 'print' insted of the 'finally' block in a function it wont be ecxecuted 