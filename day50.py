# read(), readlines() and other methods......

# with open('file.txt', 'w+') as f:
#     a = f.write("wassup amigs \n you are doing wll \n just keep going")
#     f.seek(0)
#     b = f.readlines()
#     print(b,type(a))
    


# with open(r'C:\Users\spawa\OneDrive\Desktop\coding\python\code with harry\file1.txt', 'r+') as f:
#     f.seek(0)
#     a = f.readline()
#     print(a,type(a))



# with open(r'C:\Users\spawa\OneDrive\Desktop\coding\python\code with harry\file1.txt', 'r') as f:
#     print("File content:\n")
#     print(f.read())

import os

path = r'C:\Users\spawa\OneDrive\Desktop\coding\python\code with harry\file1.txt'

# Check if file exists
if os.path.exists(path):
    print("✅ File exists!")

    with open(path, 'r') as f:
        content = f.read()
        print("📄 Content of the file:")
        print(f"'{content}'")
else:
    print("❌ File not found at the given path.")


with open('file1.txt','r') as f:
    content = f.read()
    print(content)