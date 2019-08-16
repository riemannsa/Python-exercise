import turtle
#-----------------
#bgcolour=str(input("Please input the background color:"))
#tesscolour=str(input("Please input the tess color:"))
#penSize=int(input("Please input the pen size you like:"))
#wn = turtle.Screen()
#wn.bgcolor(bgcolour)     # Set the window background color from user input
#wn.title("Hello, Tess!")      # Set the window title

#tess = turtle.Turtle()
#tess.color(tesscolour)            # Tell tess to change her color
#tess.pensize(penSize)               # Tell tess to set her pen width
#tess.shape("turtle")
#tess.speed(1)

#tess.forward(50)
#tess.left(120)
#tess.forward(50)
#----------------------------


wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

tess.penup()                # This is new
size = 20
for i in range(30):
   tess.stamp()             # Leave an impression on the canvas
   size = size + 3          # Increase the size on every iteration
   tess.forward(size)       # Move tess along
   tess.right(24)           #  ...  and turn her
tess.color("pink")
tess.stamp()
wn.mainloop()
