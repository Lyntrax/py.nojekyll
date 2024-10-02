import turtle
import time


screen = turtle.Screen()
screen.bgcolor("white")


pen = turtle.Turtle()
pen.speed(10)  

def draw_petal(turtle_obj, color):
    turtle_obj.begin_fill()
    turtle_obj.fillcolor(color)
    turtle_obj.circle(50, 60)  
    turtle_obj.left(120)
    turtle_obj.circle(50, 60) 
    turtle_obj.left(120)
    turtle_obj.end_fill()

def draw_tulip():
    pen.penup()
    pen.goto(0, -50)
    pen.pendown()
    pen.color("pink")
    pen.begin_fill()
    pen.circle(10, 360)  
    pen.end_fill()

    pen.penup()
    pen.goto(-30, -50)
    pen.pendown()
    pen.color("green")

    for _ in range(6):  
        draw_petal(pen, "green")
        pen.right(60)  

def open_tulip_slowly():
    for size in range(50, 110, 20):  
        pen.clear()
        draw_tulip()
        pen.penup()
        pen.goto(-size, -50)
        pen.pendown()
        pen.circle(size)
        time.sleep(0.5)  

open_tulip_slowly()


pen.hideturtle()
turtle.done()




