import turtle
import time
import random

turtle.setup(800,550,200,200) #设置画布大小
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25) #画笔宽度
turtle.pencolor("red")
turtle.seth(-40)
for i in  range(6):
    turtle.circle(40,80)
    turtle.pencolor("purple")
    time.sleep(1)
    turtle.circle(-40, 80)
    turtle.pencolor("blue")
    time.sleep(1)
    turtle.circle(40, 80)
    turtle.pencolor("yellow")
    time.sleep(1)
    turtle.circle(-40, 80)
    turtle.pencolor("green")
    time.sleep(1)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)