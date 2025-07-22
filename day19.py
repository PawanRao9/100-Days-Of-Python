# # BREAK AND CONTINUE........

# # for i in range(12):
# #     print("3 *", i,"=",3*(i+1))


# a = int(input("Enter the number: "))
# # for i in range(0,11):
# #     print(a,"*",i,"=",a*(i))
# # print("done")


# # for i in range(13):
# #     print(a,"*",i,"=",a*(i))
# #     if(i==10):
# #         print("skip the loop")
#         # break                    # the break will discontineue the loop after the condition satisfies

# for i in range(1,14):
   
#     if(i==10):
#        print("skip the iteration")
#        continue                    # the contineue will skip the line when teh condition satisfies and the rest will print
#     print(a,"*",i,"=",a*i)
    



def table(n):
  o = int(input("enter the no of iterations :"))
  for i in range(1,o):
    s = int(input("enter the no where u want to skip : "))

    if i == s:
       print("skip the iteration")
       continue
    if n == 0 :
        print("O")
    else :
        print(n, "*" , i ,"=",( n * i)+1)
        
    if i == 10:
       print("END")
       break    


try :
   a = int(input("Enter the number: "))
   table(a)
except ValueError:
   print("invalid input")