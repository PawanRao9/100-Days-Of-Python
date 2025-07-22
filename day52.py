#   LAMDA FUNCTION.....

''' in python , lambda function is a small anonymous finction without a name .
    it is defined using the 'lambda' keyword '''

double = lambda a : a*2
print(double(2))

avg = lambda a,b : (a+b)/2
print(avg(2,3))

avg1 = lambda a,b,c : (a+b+c)/3
print(avg1(2,3,4))

# wa can even provide a function as an arguent ;

avg = lambda a,b : (a+b)/2
print(avg(2,3))
def abc(xyz,value):
    return 3 * xyz(value,value)

print(abc(avg ,5))


p = lambda v : v * 3
s = p(3)
print('the value of p is :',s)

def a (x,value):
    return 3 + x(value)

print(a(p,12))


