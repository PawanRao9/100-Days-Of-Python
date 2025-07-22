
# timestemp = time.strftime('')

# NEED TO LEARN THE TIME CALCULATING.....


# import time

# my_time = int(input("Enter the time in seconds: "))

# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     minutes = (x // 60) % 60
#     hours = (x // 3600) % 24  # 24-hour format for hours
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)

# print("TIME UP!")


import datetime
import time

    # Get the current time
now = datetime.datetime.now()  # Get the current date and time
formatted_time = now.strftime("%H:%M:%S")  # Format the time
d = time.strftime("%d")
print("todays date is :" ,d)
while (True):    
   print(formatted_time, end="\r")  # Print time in place
   print(formatted_time ,end = "\r")
   time.sleep(1)  # Sleep for 1 second to update every second
