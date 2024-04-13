# Turtle Party Project
# by Rebecca A. Stone
# 04.13.24

import turtle

turtle.color("blue")

#size = 100
# Repeat 3 times

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()
  
#forward helper function
def move(len):
  back(-1 * len)
  
def polygon(num, size):
  for i in range(num):
    turtle.forward(size)
    turtle.left(360 / num)
    
def spiral(len, angle):
  for i in range(len, 5, -5):
    turtle.forward(i)
    turtle.right(angle)
  
spiral(75, 45)
move(150)
turtle.color("red")
spiral(100, 90)


#for n in range(3,10):
  #move(50) #forward
  #polygon(n, 100 /n)
  #back(50)
  #turtle.right(360 /7)
