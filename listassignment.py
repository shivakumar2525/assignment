#Display only even numbers from list
list=[2,3,4,5,6,7,8,9,15,16]
for n in list:
    if n % 2==0:
        print(n,end=" ")


#Display only odd numbers from list
list=[2,3,4,5,6,7,8,9,15,16]
for n in list:
    if n % 2 != 0:
        print(n,end=" ")



#Add all elements to list upto 100 which are divisible by 100
for i in range(101):
    if i%10==0:
        print(i)
