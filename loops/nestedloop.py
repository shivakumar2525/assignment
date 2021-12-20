'''n=5

for i in range(5):
    for j in range(i):
        print(" * ",end=" ")
        print("")

for i in range(n,0,1):
    for j in range(i):
        print(" * ",end=" ")

for i in range(n,0,-1):
    for j in range(i):
        print(" * ", end=" ")
    print("")'''


# import package
import turtle


# for default shape
turtle.forward(100)

# for circle shape
turtle.shape("circle")
turtle.right(60)
turtle.forward(100)

# for triangle shape
turtle.shape("triangle")
turtle.right(60)
turtle.forward(100)

# for square shape
turtle.shape("square")
turtle.right(60)
turtle.forward(100)

# for arrow shape
turtle.shape("arrow")
turtle.right(60)
turtle.forward(100)

# for turtle shape
turtle.shape("turtle")
turtle.right(60)
turtle.forward(100)
