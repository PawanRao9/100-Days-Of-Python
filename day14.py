# # # IF,ELSE,ELIF STATEMENT

# a = int(input("enter your age :"))
# print("your age is :",a)

# if a >= 18:
#     print("yes you are eligible for driving")
#     # print("system faad denge")
# else:
#     print("no you are not eligible")   
#     # print("chala ja bhosdike") 
# print("hogya")
# # # conditional operator >, <, <=, >=, ==

# print(a<18)
# print(a>18)
# print(a<=18)
# print(a>=18)
# print(a==18)

# # ELIF...

# a = int(input("Apna percentage bta:"))

# if a >= 60:
#     print("hn bhai first class")
# elif a >= 50 and a < 60:
#     print("tu averge hai")
# elif a <= 50 and a >= 35:
#     print("3rd class bokachoda")  
# else:
#     print("fail hai tu")    


# print('khatam')


# # NASTED IF ELSE.........


a = int(input("enter a number:"))

if (a==60):
    print("good number")
    if(a>=50 and a<=60):
        print('okey number')
    elif(a>=40 and a<50):
        print("average number")
    else:
        print("badddd")        
elif(a>=60 and a<=70):
    print("sahi ja rha")
    if(a>=70 and a<=80):
        print("very good buddy")
    elif(a>=80 and a<=85):
        print("bohtt badhiya")
    elif(a>=85 and a<=100):
        print("tu superb hai")
    else:
        print("padh padh")
else:
    print("padhle bahi ye coding krnese kuch nai hota")                           