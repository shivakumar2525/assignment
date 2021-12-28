class student:
    "this is student class with required data"
print(student.__doc__)
#help(student)

class student:
 def __init__(self):
    self.name='shiva'
    self.age=20
    self.marks=99

 def talk(self):
    print("hello iam:",self.name)
    print("my age is:",self.age)
    print("my marks are:",self.marks)

s1=student()
s1.talk()



class python:
    def __init__(self,name,age,batchNo):
        self.name=name
        self.age=age
        self.batchNo=batchNo
    def talk(self):
        print("my name is:",self.name)
        print("my age:",self.age)
        print("batch number:",self.batchNo)

s2=python("ranjith",25,2225356)
s2.talk()






class java:
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id
    def display(self):
        print("studentname:{}\nage:{}\nid:{}".format(self.name,self.age,self.id))

j2=java("raju",26,25486585)
j2.display()
j3=java("sri",23,454844674)
j3.display()

#instance variables          $object level

#inside Constructor by self variable:
class employee:
    def __init__(self):
        self.eno=25
        self.name="shivakumar"
        self.esal=20000

e=employee()
print(e.__dict__)


#Inside Instance Method by self var.:
class test:
    def __init__(self):
        self.a=20
        self.b=30
    def m1(self):
        self.c=50
t=test()
t.m1()
print(t.__dict__)


#Outside of the class by obj. ref. Var.:
class tests:
    def __init__(self):
        self.a=20
        self.b=33
    def m2(self):
        self.c=88
t2=tests()
t2.m2()
t2.d=225
print(t2.__dict__)

#How to access Instance variables:
class Test:
  def __init__(self):
    self.a=10
    self.b=20
  def display(self):
    print(self.a)
    print(self.b)
   # del self.b      #delete inside class instance variable with self
t=Test()
#del t.b            #delete out class instance variable with obj refere
t.display()
print(t.a,t.b)



#static variables  $class level

class test:
    x=20
    def __init__(self):
        self.y=30
t1=test()
t2=test()
 #del test.x    $delete the static variable
print('t1:',t1.x,t2.y)
print('t2:',t1.x,t2.y)
test.x=365
t1.y=50
print('t1:',t1.x,t1.y)
print('t2:',t1.x,t2.y)


#local variables   $method level
class Test:
  def m1(self):
    a=1000
    print(a)
  def m2(self):
    b=2000
    #print(a)    #NameError: name 'a' is not defined
    print(b)
t=Test()
t.m1()
t.m2()

#garbage collector(destroying objects
class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, "destroyed")
pt1 = Point()
pt2 = pt1
print (id(pt1), id(pt2))                  # prints the ids of the obejcts
del pt1


#Class Inheritance:
class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print ("Calling parent constructor")

   def parentMethod(self):
      print ('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)

class Child(Parent):    # define child class
   def __init__(self):
      print ("Calling child constructor")

   def childMethod(self):
      print ('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method

#overridings method
class Parent:                # define parent class
   def myMethod(self):
      print ('Calling parent method')

class Child(Parent):         # define child class
   def myMethod(self):
      print ('Calling child method')

c = Child()          # instance of child
c.myMethod()         # child calls overridden method


#data hiding
class JustCounter:
   __secretCount = 0

   def count(self):
      self.__secretCount += 1
      print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
#print (counter.__secretCount)
print(counter._JustCounter__secretCount)

#polymorphism

class India():
	def capital(self):
		print("New Delhi is the capital of India.")

	def language(self):
		print("Hindi is the most widely spoken language of India.")

	def type(self):
		print("India is a developing country.")

class USA():
	def capital(self):
		print("Washington, D.C. is the capital of USA.")

	def language(self):
		print("English is the primary language of USA.")

	def type(self):
		print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
	country.capital()
	country.language()
	country.type()

#2 use functions and obj

def func(obj):
	obj.capital()
	obj.language()
	obj.type()

obj_ind = India()
obj_usa = USA()

func(obj_ind)
func(obj_usa)


#encapsulation

# Python program to
# demonstrate protected members


# Creating a base class
class Base:
    def __init__(self):
        self._a = 2   #protected
        self._b = 30
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling protected member of base class: ")
        print(self._a)
        print(self._b)


obj1 = Derived()

obj2 = Base()

print(obj2._a)
print(obj2._b)

#encapsulation with private number

class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "hello"



class Derived(Base):
    def __init__(self):

        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)

obj1 = Base()
print(obj1.a)


import calendar
year=2021
month=8
print(calendar.month(year,month))


#Abstraction method
from abc import ABC,abtractmethod
class car (ABC):
    def meilege(self):
        pass

class tesla(car):
    def meilege(self):
        print("the meilage is 30kmph")

class maruthi(car):
    def meilege(self):
        print("the meilage is 120kmph")

class benz(car):
    def meilege(self):
        print("the meilage is 20kmph")

t=tesla()
t.meilege()

m=maruthi()
m.meilege()

b=benz()
b.meilege()
