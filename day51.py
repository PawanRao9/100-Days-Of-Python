# # seek(), tell() and other functions..........

# import io
# from io import StringIO

# # with open('file1.txt','r') as f:
# #     print(type(f))
# #     f.seek(3)      # the seel() allows you to move the current position with a file to specific point,
# #     data = f.read(5)
# #     print(data)


# # with open("file.txt","r") as f:
# #     a = f.tell()  # tell() returns the current position of the file pointer,
# #     print(a)
# #     b = f.read()
# #     print(b)   

# # with open('file2.txt','w') as f:
# #     f.write('Hello, world!')
# #     f.truncate(5)    # the truncate() function truncates the file to the specified size. basicly it removes the rest of the file.
# # with open('file2.txt','r') as f:
# #     print(f.read())  # Output: Hello

# with open("file1.txt","r") as f:
#     f.seek(10)
#     print(f.tell())
#     data = f.read(5)
#     print(data)  # Output: world


with open("file3.txt","w") as f3:
    f3.write("Hello, world!")
    f3.truncate(5)

with open("file3.txt","r") as f3:
    print(f3.read())  # Output: Hello