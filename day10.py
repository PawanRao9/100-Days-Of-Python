# # USER INPUT IN PYTHON...........

# # in python we can directly take user input by input function...


p = input("enter your name :")
print(f"Nice meating you {p}")
a = int(input("Suru karne ke liye 1 dabaye: "))

if a == 1:
    print("1 - Addition of two numbers \n2 - Addition of three numbers \n3 - Subtraction of two numbers \n4 - Subtraction of three numbers")
    choice = int(input("app iss me se kya krnaa pasnd karenge: "))
    
    if choice == 1:
        x = int(input("Enter 1st number: "))
        y = int(input("Enter 2nd number: "))
        print("The addition will be:", (x + y))
        
    elif choice == 2:
        x = int(input("Enter 1st number: "))
        y = int(input("Enter 2nd number: "))
        z = int(input("Enter 3rd number: "))
        print("The addition will be:", (x + y + z))
        
    elif choice == 3:
        x = int(input("Enter 1st number: "))
        y = int(input("Enter 2nd number: "))
        print("The subtraction will be:", (x - y))
        
    elif choice == 4:
        x = int(input("Enter 1st number: "))
        y = int(input("Enter 2nd number: "))
        z = int(input("Enter 3rd number: "))
        print("The subtraction will be:", (x - y - z))
        
    else:
        print("Bhai tumse na ho payega!")
else:
    print("Invalid input. Please press 1 to start.")
