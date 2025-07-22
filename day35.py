#   FOR LOOP WITH ELSE

for i in range (12): 
    print(i)
    if i ==  10:
        break
     
      
else:
    print("no more i")

'''the else block will be excecuted after all iterations are completed.
the program exits the loop after the else block is excecuted'''    

i = 0
while i < 12:
    print(i)
    i += 1
    if i == 10:
      break
else:
    print("khatam")    