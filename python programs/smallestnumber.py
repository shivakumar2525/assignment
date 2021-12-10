a,b,c=10,20,30

if(a <= b and a <= c):
    print(a,"is smallest")
elif(b <= c and b <= a):
    print(b,"is smallest")
else:
    print(c,"is smallest")



#two variable
a=10
b=20

if a<=b:
    print(a,"is smallest")
else:
    print(b,"is largest")




a=int(input("Enter your first number:"))
b=int(input("Enter your second number: "))
if(a<b):
    print("{} is smallest".format(a))
elif(a<b):
    print("{} is smallest".format(b))
else:
    print("{} and {} are equal".format(a,b))




a=10
b=20
c=30
print(min(a,b,c))

