# RECURSION ......

# def fact_orel(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n*fact_orel(n-1)
# a = int(input("enter a num: "))
# print(fact_orel(a))    

# recursion = it means making a function calling itself again and agnain until some conditions satisfy in a function


# def fibonacci(n):
#     fibonacci_sequence =[]
#     a,b = 0,1
#     for _ in range(n):
#         fibonacci_sequence.append(a)
#         a ,b=b,a+b
#     return fibonacci_sequence


# a = int(input("enter a number:"))
# print("the fibonacci series :",fibonacci(a))    

def login():
    # Preset username and password
    valid_username = "BeastBoy"
    valid_password = "pawan@123"

    print("Welcome to the Fibonacci Sequence Generator!")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == valid_username and password == valid_password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password. Please try again.")
        return False
login()    