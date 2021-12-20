'''number=int(input("enter a number:"))
for number in range(100):
    print(number<=100)
else:
    print("out of range")'''




s="Sunny Leone"; i=0;
for x in s :
  print(x)
  print("The character present at ",i,"index is :",x)
  i=i+1



r=range(10,20,2)
for i in r:
  print(i)



r=list(range(10))
print(r)


for x in range(20,5,-2):
  print(x)

#i = 0;
#while True:
 #   i = i + 1;
  #  print("Hello", i)
'''for number in range(3):
  print("--------------------------------------")
  print("iam outer loop interaction="+str(number))
  for another_number in range(4):
    print("*************************************")
    print("iam inner loop interaction="+str(number))'''



# Print the below statement 3 times
for number in range(3) :
    print("-------------------------------------------")
    print("I am outer loop iteration "+str(number))
    # Inner loop
    for another_number in range(5):
        print("****************************")
        print("I am inner loop iteration "+str(another_number))



