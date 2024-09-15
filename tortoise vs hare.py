#Name: Hasin Shadab Rahman                                                         UID:U87513234

# Import required modules (random, turtle, time)
# Configure turtle screen and settings
# Create turtle objects for:
# Tortoise (green turtle shape)
# Hare (classic shape)
# Finish line
# Start line
# Start/finish labels
# Message display
# Define functions:
# tortoise_move() - handles tortoise movement logic
# hare_move() - handles hare movement logic
# Set starting positions (-100, 0) and (100, 50)
# Main game loop:
# Call tortoise and hare movement functions to update positions
# Move turtles to new positions
# Increment clock
# After loop, check final positions to determine winner
# Display win message centered at top of screen
# Pause for 5 seconds to display result
# Hold screen until click to exit
# The key aspects are:
# Utilizing multiple turtles for visuals
# Encapsulating move logic in functions
# Looping until a winner is determined
# Printing graphical output for start/end state
import random
import turtle
import time

# Create screen 
screen = turtle.Screen()
screen.setup(500,500)
screen.title("Tortoise vs Hare")

# Create turtles
tortoise = turtle.Turtle()
tortoise.shape('turtle')
tortoise.color('green')
tortoise.penup()
tortoise.setpos(-100,0)

hare = turtle.Turtle()
hare.shape('classic')
hare.color('blue')
hare.penup()
hare.setpos(-100,50)

message = turtle.Turtle()
message.hideturtle()
message.penup()
message.setpos(0,200)
message.write("On Your Mark...Get Set...Go...And they're off", align="center", font=("Arial", 14, "bold"))

# Create labels
# Create starting line
start = turtle.Turtle()
start.hideturtle()
start.penup()
start.setpos(-100, 0)
start.pendown()
start.left(90) # face upwards
start.forward(50) 
start.write("Start", font=("Arial", 12, "normal"))

# Create finish line  
finish = turtle.Turtle()
finish.hideturtle()
finish.penup()
finish.setpos(100, 0)
finish.pendown()
finish.left(90) # face upwards
finish.forward(50)
finish.write("End", font=("Arial", 12, "normal"))


# Functions to control turtle movement
def tortoise_move(current_pos):
    move = random.randint(1,10)
    if move >= 1 and move <= 5: # Fast plod
        current_pos += 3
    elif move >= 6 and move <= 7: # Slip
        current_pos -= 3
    else: # Slow plod
        current_pos += 1
        
    if current_pos < -100:
        current_pos = -100
    elif current_pos > 100:
        current_pos = 100
    return current_pos

def hare_move(current_pos):
    move = random.randint(1,10)
    if move == 1 or move == 2: # Big slip
        current_pos -= 5
    elif move >= 3 and move <= 5: # Big hop
        current_pos += 7
    elif move >= 6 and move <= 8: # Small hop
        current_pos += 1
    else: # Small slip
        current_pos -= 2
        
    if current_pos < -100:
        current_pos = -100
    elif current_pos > 100:
        current_pos = 100
    return current_pos
        
# Main game loop
clock = 0
tortoise_pos = -100
hare_pos = -100

# Create turtle to display messages
message = turtle.Turtle()
message.hideturtle()
message.penup()

# Main game loop
while tortoise_pos < 100 and hare_pos < 100:
   tortoise_pos = tortoise_move(tortoise_pos)
   hare_pos = hare_move(hare_pos)
   tortoise.setpos(tortoise_pos, 0)
   hare.setpos(hare_pos, 50)
   clock += 1

if tortoise_pos >= hare_pos:
    message.setpos(100,-100)
    message.write("Tortoise wins in "+str(clock)+" seconds!", align="center", font=("Arial", 14, "bold"))

else:  
  message.setpos(100,-100)
  message.write("Hare wins in "+str(clock)+" seconds!", align="center", font=("Arial", 14, "bold"))

time.sleep(2) # Pause for 2 seconds

screen.exitonclick() # Exit on click