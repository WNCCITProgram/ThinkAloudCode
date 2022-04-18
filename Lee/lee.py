import turtle
import random
line=random.randint(50,100)
for x in range (0,line):
    length=random.randint(25,100)
    rotate=random.randint(1,365)
    turtle.forward(length)
    turtle.right(rotate)
turtle.exitonclick()