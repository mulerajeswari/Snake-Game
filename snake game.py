import turtle
import time
import random

# Game settings
delay = 0.1
score = 0
highestscore = 0
bodies = []

# Setup screen
win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("pink")
win.setup(width=600, height=600)
win.tracer(0)

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("blue")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Scoreboard
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(-250, 260)
score_display.write("Score: 0 | High Score: 0", font=("Arial", 15, "bold"))

# Movement functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# Key bindings
win.listen()
win.onkey(go_up, "Up")
win.onkey(go_down, "Down")
win.onkey(go_left, "Left")
win.onkey(go_right, "Right")

# Game loop
while True:
    win.update()

    # Border collision
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for body in bodies:
            body.goto(1000, 1000)
        bodies.clear()
        score = 0
        delay = 0.1
        score_display.clear()
        score_display.write(f"Score: {score} | High Score: {highestscore}", font=("Arial", 15, "bold"))

    # Eating food
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Add new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("darkred")
        new_segment.penup()
        bodies.append(new_segment)

        # Increase score
        score += 10
        if score > highestscore:
            highestscore = score
        delay = max(0.05, delay - 0.001)

        score_display.clear()
        score_display.write(f"Score: {score} | High Score: {highestscore}", font=("Arial", 15, "bold"))

    # Move the segments
    for i in range(len(bodies) - 1, 0, -1):
        x = bodies[i - 1].xcor()
        y = bodies[i - 1].ycor()
        bodies[i].goto(x, y)

    if bodies:
        bodies[0].goto(head.xcor(), head.ycor())

    move()

    # Body collision
    for segment in bodies:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for body in bodies:
                body.goto(1000, 1000)
            bodies.clear()
            score = 0
            delay = 0.1
            score_display.clear()
            score_display.write(f"Score: {score} | High Score: {highestscore}", font=("Arial", 15, "bold"))

    time.sleep(delay)

win.mainloop()
