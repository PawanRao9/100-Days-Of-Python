import time
import datetime

def livetime():
 while True:

  now = datetime.datetime.now()
  live = now.strftime('%H:%M:%S')
  print(live, end ="\r")
  time.sleep(1)


hour = int(time.strftime('%H'))

# print("the time is :",hour,"HOURS")
# print(int(input("enter hour: ")))
a = str(input("Enter your name: "))
if(hour > 0 and hour <= 12):
    print("GOOD MORNING",a)
elif(hour > 12 and hour <= 17):
    print("GOOD AFTERNOON",a)
elif(hour > 17 and hour <= 22):
    print("GOOD EVENING",a)
else:
    print("GOOD NIGHT",a)

