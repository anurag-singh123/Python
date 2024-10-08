import turtle

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle named 'flower'
flower = turtle.Turtle()
flower.speed(10)  # Set the speed to maximum

# Function to draw a petal
def draw_petal():
    flower.color("red")
    flower.circle(100, 60)
    flower.left(120)
    flower.circle(100, 60)
    flower.left(120)

# Function to draw the flower
def draw_flower():
    for _ in range(6):
        draw_petal()
        flower.right(60)

# Draw the flower
draw_flower()

# Draw the stem
flower.color("green")
flower.right(90)
flower.forward(300)

# Hide the turtle
flower.hideturtle()

# Keep the window open
turtle.done()
