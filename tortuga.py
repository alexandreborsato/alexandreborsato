import turtle
from turtle import *
import tkinter as _tkinter

# Create a new turtle object
t = turtle.Turtle()

# Set the turtle's speed (1-10, with 1 being the slowest)
t.speed(5)

# Draw a square
for i in range(4):
    t.forward(100)
    t.right(90)

# Move the turtle to a new position
t.penup()
t.goto(200, 200)
t.pendown()

# Draw a circle
t.circle(50)

# Change the turtle's color
t.color("blue")

# Draw a triangle
t.penup()
t.goto(-100, -100)
t.pendown()
for i in range(3):
    t.forward(100)
    t.left(120)

# Keep the window open until it's closed
turtle.done()

