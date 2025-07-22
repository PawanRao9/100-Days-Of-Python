print("hello world")


import os

# Create "python" directory if it doesn't exist
if not os.path.exists("python"):
    os.mkdir("python")

# Loop to create folders and .py files inside them
for i in range(100):
    folder_name = f"day{i+1}"
    folder_path = os.path.join("python", folder_name)

    # Create folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    # Create a Python file inside the folder
    file_path = os.path.join(folder_path, f"{folder_name}.py")
    with open(file_path, 'w') as f:
        f.write(f"# This is {folder_name}.py\n")

print("Folders and files created successfully.")
