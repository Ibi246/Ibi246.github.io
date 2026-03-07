'''
India Isaacson
I added multiple new houses and centered the houses and trees better
I then also added more detail to the snowman
'''

#first I import turtle and math modules
import turtle
import math

def setup_turtle():
    """Initialize turtle with standard settings"""
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    screen = turtle.Screen()
    screen.title("Turtle Graphics Assignment")
    return t, screen


def draw_rectangle(t, width, height, fill_color=None):
    """Draw a rectangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()

def draw_square(t, size, fill_color=None):
    """Draw a square with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    if fill_color:
        t.end_fill()


def draw_triangle(t, size, fill_color=None):
    """Draw an equilateral triangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
        t.end_fill()


def draw_circle(t, radius, fill_color=None):
    """Draw a circle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()

def draw_curve(t, length, curve_factor, segments=10, fill_color=None):
    """
    Draw a curved line using small line segments
    
    Parameters:
    - t: turtle object
    - length: total length of the curve
    - curve_factor: positive for upward curve, negative for downward curve
    - segments: number of segments (higher = smoother curve)
    - fill_color: optional color to fill if creating a closed shape
    """
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
        
    segment_length = length / segments
    # Save the original heading
    original_heading = t.heading()
    
    for i in range(segments):
        # Calculate the angle for this segment
        angle = curve_factor * math.sin(math.pi * i / segments)
        t.right(angle)
        t.forward(segment_length)
        t.left(angle)  # Reset the angle for the next segment
    
    # Reset to original heading
    t.setheading(original_heading)
    
    if fill_color:
        t.end_fill()
        
def jump_to(t, x, y):
    """Move turtle without drawing"""
    t.penup()
    t.goto(x, y)
    t.pendown()

colors=["red", "blue", "brown", "yellow", "purple", "green", "lightblue", "black",  "cyan"]

def draw_sun(t):
    jump_to(t, -200, 150)
    draw_circle(t, 50, fill_color="yellow")

def draw_house(t):
     draw_triangle(t, 100, fill_color=colors[0])
     t.forward(10)
     draw_square(t, 80, fill_color=colors[7])   

def draw_tree(t):
    draw_circle(t, 70, fill_color="white")
    t.backward(25)
    draw_rectangle(t, 50, 100, fill_color="tan") 
    draw_curve(t, 100, 5, fill_color="tan")

def draw_clouds(t):
    jump_to(t, -100, 200)
    draw_circle(t, 30, fill_color="white")
    jump_to(t, -70, 220)
    draw_circle(t, 30, fill_color="white")
    jump_to(t, -40, 200)
    draw_circle(t, 30, fill_color="white")
    jump_to(t, 50, 180)
    draw_circle(t, 30, fill_color="white")
    jump_to(t, 80, 200)
    draw_circle(t, 30, fill_color="white")
    jump_to(t, 110, 180)
    draw_circle(t, 30, fill_color="white")

def draw_snowman(t):
    # bottom circle
    jump_to(t, -250, -100)
    draw_circle(t, 40, fill_color="white")  
    # middle circle
    jump_to(t, -250, -60)
    draw_circle(t, 30, fill_color="white")  
    jump_to(t, -250, -20)
    # head circle 
    draw_circle(t, 20, fill_color="white")
    #eyes
    jump_to(t, -260, 0)
    draw_circle(t, 5, fill_color="black")  
    jump_to(t, -240, 0)
    draw_circle(t, 5, fill_color="black") 
    #nose
    jump_to(t, -245, -10)
    draw_triangle(t, 10, fill_color="orange")
    #mouth
    jump_to(t, -265, -15)   
    draw_curve(t, 30, -3, segments=5)
    #arms
    jump_to(t, -285, -35)
    t.setheading(160)
    t.pensize(5)
    t.forward(40)
    t.backward(50)
    jump_to(t, -215, -35)
    t.setheading(20)
    t.forward(40)
    t.backward(50)
    t.pensize(1)  # reset pen size
    #draw buttons
    jump_to(t, -250, -30)
    draw_circle(t, 5, fill_color="black")
    jump_to(t, -250, -50)
    draw_circle(t, 5, fill_color="black")
    jump_to(t, -250, -70)
    draw_circle(t, 5, fill_color="black")

def draw_ground(t):
    jump_to(t, -300, -100)
    draw_rectangle(t, 2000, 800, fill_color="white")

def draw_scene(t):
    screen = t.getscreen()
    screen.bgcolor("skyblue")  
    #draw sun
    draw_sun(t)  
    #draw the houses
    jump_to(t, 0, -20)
    draw_house(t)
    jump_to(t, -100, -20)
    draw_house(t)
    jump_to(t, -200, -20)
    draw_house(t)
    jump_to(t, 500, -20)
    draw_house(t)
    jump_to(t, 400, -20)
    draw_house(t)
    jump_to(t, 300, -20)
    draw_house(t)   
    #draw a tree with snow and a branch
    jump_to(t, 200, 0)
    draw_tree(t)
    #draw two clouds
    jump_to(t, -100, 200)
    draw_clouds(t)
    jump_to(t, 50, 180)
    #draw the snowy grass
    draw_ground(t)
    #draw a snowman
    draw_snowman(t)  
    
    
    
    

# This is the main() function that starts off the execution
def main():
    t, screen = setup_turtle()
    draw_scene(t)
    screen.mainloop()
    
# if this script is executed, call the main() function
# meaning when is file is run directly
if __name__ == "__main__":
    main()