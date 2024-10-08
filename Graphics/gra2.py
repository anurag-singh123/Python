import turtle

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle named 'artist'
artist = turtle.Turtle()
artist.speed(0)  # Set the speed to maximum

# Function to draw a star
def draw_star(size, color):
    artist.color(color)
    artist.begin_fill()
    for _ in range(5):
        artist.forward(size)
        artist.right(144)
    artist.end_fill()

# Function to draw a spiral of stars
def draw_spiral_of_stars():
    colors = ["red", "yellow", "blue", "green", "purple", "orange"]
    size = 30
    for i in range(60):
        draw_star(size, colors[i % len(colors)])
        artist.forward(i * 5)
        artist.right(144)

# Function to draw a circle pattern
def draw_circle_pattern(radius, color):
    artist.color(color)
    for _ in range(36):
        artist.circle(radius)
        artist.right(10)

# Function to draw a complex pattern
def draw_complex_pattern():
    draw_spiral_of_stars()
    artist.penup()
    artist.goto(-150, -150)
    artist.pendown()
    draw_circle_pattern(100, "white")
    artist.penup()
    artist.goto(150, -150)
    artist.pendown()
    draw_circle_pattern(100, "white")
    artist.penup()
    artist.goto(0, 150)
    artist.pendown()
    draw_circle_pattern(100, "white")

# Draw the complex pattern
draw_complex_pattern()

# Hide the turtle
artist.hideturtle()

# Keep the window open
turtle.done()
