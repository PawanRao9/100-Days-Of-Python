# LOCAL-VARIABLE AND GLOBAL-VARIABLE ........

s = 234
# print("Global variable a =", a) 

def my_function():
    a = 123
    global s # This line is used to declare that we want to use the global variable s inside the function
    s = 124
    print(f"the global variable in local scope is {s}")
    print(f"the local a is {a}")

print(my_function())
print(f"the global a is {s}")  # Output: 234
