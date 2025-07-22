# WHILE LOOP

# a = int(input("Enter a number: "))

# while(a<=5):
#     print("ola amigo")
#     a += 1


# while(a >= 0):
#     print(a)
#     a = a-1
import pyttsx3
import time

Omm = pyttsx3.init()
voices = Omm.getProperty('voices')
Omm.setProperty('voice', voices[0].id)

while True:
    try:
        a = int(input("Enter a number: "))
    except ValueError:
        print("Enter a valid number!")
        continue

    if a <= 0:
        print("Please enter a number greater than 0.")
        continue

    for i in range(a):
        Omm.say("Har Har Mahadev!")
        Omm.runAndWait()
        time.sleep(1)
    break  # exit after speaking once
