'''s={1,2,3,4,5}
print(s)
print(type(s))

l = [10,20,30,40,10,20]
s=set(l)
print(s)


s=set(range(5))
print(s)

s=set()
print(s)

s={1,2,3,4,5}
i=[20,50,60,40]
s.update(i,range(5))
print(s)


s1={2,3,4,5,6}
s2=s1.copy()
print(s1)

print(s1.pop())
print(s1)
s1.remove(4)
print(s1)

d={10,20,30,50}
d.discard(10)
print(d)
d.discard(100)
print(d)
d.clear()
print(d)'''


x={10,20,30,40}
y={30,40,50,60}

print(x|y)

print(x&y)

print(x-y)
print(y-x)

print(x^y)


s=set("shivakumar")
print(s)
print('g' in s)
print('s' in s)


s={x*x for x in range(5)}
print(s)



#assignment
#Write a program to eliminate duplicates present in the list

duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(list(set(duplicate)))


# Write a program to print different vowels present in the given word
vowels =['a','e','i','o','u']
string = input("Enter any statement : ")
data = set(string)
result = data.intersection(vowels)
print("Vowels present in given statement :",result)