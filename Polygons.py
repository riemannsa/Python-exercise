#Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):

#An equilateral triangle
#A square
#A hexagon (six sides)
#An octagon (eight sides)

import turtle
color= str (input("Please input color you want for t1."))
n=int(input("Plesae input the number of sides you want for the polygons:"))
wn=turtle.Screen()
t1=turtle.Turtle()
t1.color(color)
angle=int(360/n)
for i in range(n):
    t1.forward(60)
    t1.left(angle)
    
