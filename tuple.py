t=1,30,21,66,50,45
print(t)
print(type(t))
t1=()
print(t1)
print(type(t1))


list=[1,2,3,4]
t=tuple(list)
print(t)
print(type(t))

print(t[1:3])
print(t[2,100])


t1=1,2,22,66,65,45,25,33
t2=5,25,20,12,33
t3=t1+t2
print(t3)
t2=t1*3
print(t2)

print(len(t1))
print(t1.count(2))
print(t1.index(25))

#print(t1.index(1122))


t2=sorted(t1)
print(t2)
t2=sorted(t1,reverse=True)
print(t2)

print(t1)
print(min(t1))
print(max(t1))


#tuple packing and unpacking
a=10;b=20;c=30;
t=a,b,c
print(t)

t=10,20,30
a,b,c=t
print("a=",a,"b=",b,"c=",c)

t= ( x**2 for x in range(1,6))
print(type(t))
for x in t:
  print(x)


#Write a program to take a tuple of numbers from the keyboard and print its sum and average?

some_tuple=2,3,5,6,9
def average(some_tuple):
    print(sum(some_tuple)/len(some_tuple))

average(some_tuple)
