# EXCEPTION HANDELING ...........

'''exception handeling is the process of responding to the unwanted or unexpected events when a computer program runs, 
EXCEPTION handeling deals with these events to avoid the program or system crashing'''

# a =  input('enter a num :')
# # b = int(input('enter b num :'))

# print(f'the multiplication table of {a} is:')

# try :                          # the 'try' block checks weather an exception is occoured or not and send it to the 'except' block if the excepion arises
#   for i in range(1,11):
#       print(f'{int(a)} * {i} = {int(a)*i}')
# except Exception as e:         # the ' except ' block tells about the type of exception occourd
#    print(f"the error is {e}")      
# finally :                              # "finally" block will print weather the exception occourd or not
#    print("this line will be printed")
# print("this line will also be printed")



while(True):
 try :
   num = int(input("enter a num :"))
   a = (5,3,4)
   print(a[num])
 except IndexError:
   print("invalid index")
 except ValueError:
   print("it is not a integer")      
 except TypeError:
   print("type right thing") 
 except MemoryError:
   print("memory error occoured")  
    

