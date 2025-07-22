# FILE HANDELING ........



''' python provides a open() function to open a file .
    it tales two arguments : the name of the file and mode which the file shud be opend
    mode can be 'r' for read , 'w' for write , 'a' for appending.'''


f = open("file.txt","r")
# b = open("file.txt","r")

text = f.read()
print(text)
f.close()  

# f1 = open("file.txt","w") # this will delete the previous content of the file

# f2 = open("file.txt","a") # this will add the content at the end of the file

# f3 = open("file.txt","x") # this will create a new file if the file is not present

f4 = open("file1.txt","w")
f4.write("wassup bruh!")
b = f4.read()
print(b)
f4.close()

with open("file1.txt","r") as f5:
    f.write("hello amigo!")


# THIS THING IS NOT WORING IN MY SYSTEM..........