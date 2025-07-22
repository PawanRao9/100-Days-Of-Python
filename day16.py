# MATCH CASE STATEMENT.....

print("whoem do you think as the father of LUCKY")
print("for the options enter 1:")

while (True):
    print("1 - ROHIT\n 2 - PANKAJ\n 3 - avhisekh\n 4 - ashutosh\n")

    a = int(input("enter your option:"))

    match a:
      case 1:
         print("wrong buddy")
      case 2:
         print("well tried") 
      case 3:
         print("Absolutely correct")
      case 4:
         print("first know and then come")
      case _:\
         print("get the heal out of here")

    print("END")
    break
            
    # THEEK KARNA HAI 