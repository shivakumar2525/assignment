list=["shiva",20,"srikanth",30,"gouthami",50,60,80]
print(list[0])
print(list[1:5])
print(list[1:5:2])
print(list[-1])
print(list[-1:-6:1])
print(len(list))
print(list*2)

list[2]=200
print(list)


n=[0,1,2,3,4,5,6,7,8,9,10]
i=0

while i<len(n):
    print(n[i])
    i=i+1


for n1 in n:
    print(n1)


print(len(n))
print(n.count(2))
n1=[20,30,50,64,22]
print(n1.index(22))


print(list)
list.append("SHIVA")
print(list)
list.insert(2,"kumar")
print(list)
list.extend(300)
print(list)
list.extend(n1)
print(list)
