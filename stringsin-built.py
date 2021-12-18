#strings in-built methods

s="wellcome shivakumar"
print(len(s))

print('g' in s)
print('s' in s)

print(s.find('a'))

s1="dsgugdfhkhofhh"
print(s1.count('g'))
print(s1.count('f'))
print(s1.count('g',1,8))


s2="Learning Python is very difficult"
print(s2)
s3=s2.replace("difficult","easy")
print(s3)

print(id(s2))
print(id(s3))
print(s3)


print(s.split())
print(s.split('-'))

t = ('shiva', 'uday', 'hari')
s='-'.join(t)
print(s)
s1=':'.join(t)
print(s1)

print(s2.upper())
print(s2.lower())
print(s2.swapcase())
print(s2.title())
print(s2.capitalize())


print(s2.startswith('learning'))

s2="Learning Python is very difficult"
print(s2.endswith('very'))
print(s2.isalnum())
print(s2.isalpha())
print(s2.isdigit())


name='shiva'; salary=100000 ; age=48
print("{} 's salary is {} and his age is {}".format(name,salary,age))

print("{0} 's salary is {1} and his age is {2}".format(name,salary,age))

print("{x} 's salary is {y} and his age is {z}".format(z=age,y=salary,x=name))

