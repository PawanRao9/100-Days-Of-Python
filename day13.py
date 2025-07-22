# STRING METHODS....

# UPPER CASE

p = "pawan"
print(len(p))
print(p.upper()) #this is used for converting into upper case , and also strings are immutable

q = "PAWAN"
print(p.lower()) #this is used for printing the lower case

print(p.rstrip("!")) # it will remove the space at the end if exists


print(p.replace("pawan","ducati")) #it is used for  replacing the string

print(q.split(" ")) # it is used for converting the string into "LIST"

print(p.capitalize()) # this is used for capitalise the only first charactor of the string, and the rest will be in lower case

print(p.center(25)) # it will take the string into center as per the parameters space given

print(p.count("a"))# it will count the charactors that we want to count,also it can count the repetation of the string as well

 
str1 = "juice pilado mausambi AB 09 ka"
print(str1.endswith("ka")) # it will show the end string that is endes with

print(str1.endswith("ka,22,25"))
print(len(str1))

str2 = "cheen tapak dum dum"
print(str2.find("tapak"))#this method will show the loaction of the string

print(str1.isalpha())#the method shows true only is the string contains A-Z, a-z and 0-9, either the output will be false it is called the "ALPHA NUMERIC STRING"

print(str1.isprintable())


print(str1.swapcase()) #it will the upper case into lower and the lower case to upper








p = "1235pawan"
print(p.isalpha()) # the isalpha returns True only if the string cotains "ALPHABATES" in uppercase or in lower case

q = "aksjd"
print(q.isalpha())