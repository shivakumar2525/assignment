'''import sys
print(type(sys.argv))





from sys import argv
sum=0
args=argv[1:]
for x in args :
  n=int(x)
  sum=sum+n
print(sum)'''






#output arguments
print("helloworld")
print("hello \nworld")

print(10*"hello\n")
print(10*"shiva\n\t")
print("tuniki\n\tshiva\n\t  kumar")

print("shiva"+"kumar")
print("shiva","kumar")

a,b,c=20,30,52
print("the values are:",a,b,c)

print(a,b,c,sep=":")
print("hello",end=' ')
print("shiva",end=' ')
print("kumar",end=' ')


s="Gm" ; a=28; s1="java"; s2="Python"
print("Hello",s,"Your Age is",a)
print("You are teaching",s1,"and",s2)


#%i====>int  	%d====>int     	%f=====>float  	%s======>String
a=10 ; b=20; c=30; s="Gm" ; list=[10,20,30,40]
print("a value is %i" %a)
print("b value is %d and c value is %d" %(b,c))
print("Hello %s ...The List of Items are %s" %(s,list))






name="Gm"; salary=10000; gf="Sunny"
print("Hello {0} your salary is {1} and Your Friend {2} is waiting".format(name,salary,gf))
print("Hello {x} your salary is {y} and Your Friend {z} is waiting".format(x=name,y=salary,z=gf))



s="shiva"
print(s)
del s
print(s)


a=10
b=20

if (a >= b):
    largest number=a,
else
    (a <= b)
    largest number=b

print("largest number is:",largestnumber)







