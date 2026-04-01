import turtle
import random
import winsound

# screen
w, h = 500, 500
screen = turtle.Screen()
screen.setup(w, h + 60)
screen.bgcolor("black")
screen.title("Snake Game 🐍")
screen.tracer(0)

# grid settings
cell = 20

# variables
d = 120
score = 0
high_score = 0
level = 1
paused = False
game_running = False
snake_color = "lime"

# SAFE AREA (IMPORTANT FIX)
margin = cell
min_x = -w//2 + margin
max_x = w//2 - margin
min_y = -h//2 + margin
max_y = h//2 - margin

# movement
offsets = {
    "up": (0, cell),
    "down": (0, -cell),
    "left": (-cell, 0),
    "right": (cell, 0)
}

# snake
pen = turtle.Turtle()
pen.shape("square")
pen.penup()

# food
food = turtle.Turtle()
food.shape("circle")
food.penup()

# score
score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.penup()
score_pen.goto(0, h//2 + 10)
score_pen.color("white")

# bottom name
name_pen = turtle.Turtle()
name_pen.hideturtle()
name_pen.penup()
name_pen.goto(0, -h//2 - 20)
name_pen.color("white")
# name_pen.write("GAME BY CHANDAN PRAJAPAT",
#                align="center", font=("Arial", 10, "bold"))

# text
text_pen = turtle.Turtle()
text_pen.hideturtle()
text_pen.penup()
text_pen.color("white")

# ---------------- FUNCTIONS ---------------- #

def draw_border():
    b = turtle.Turtle()
    b.hideturtle()
    b.color("white")
    b.penup()
    b.goto(min_x - cell//2, min_y - cell//2)
    b.pendown()

    b.goto(max_x + cell//2, min_y - cell//2)
    b.goto(max_x + cell//2, max_y + cell//2)
    b.goto(min_x - cell//2, max_y + cell//2)
    b.goto(min_x - cell//2, min_y - cell//2)

def spawn_food():
    global khanaT, food_color

    x = random.randrange(min_x, max_x, cell)
    y = random.randrange(min_y, max_y, cell)

    khanaT = (x, y)

    food_color = random.choice(["red","blue","yellow","purple","cyan"])
    food.goto(khanaT)
    food.color(food_color)

def dist(p1,p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5

def update_score():
    score_pen.clear()
    score_pen.write(f"Score: {score}   High: {high_score}   Level: {level}",
                    align="center", font=("Arial", 14, "bold"))

def reset_game():
    global saap, kata, score, d, paused, game_running, level, snake_color

    text_pen.clear()
    pen.clearstamps()

    game_running = True
    paused = False

    saap = [[0,0],[0,cell],[0,cell*2]]
    kata = "up"
    score = 0
    level = 1
    d = 120
    snake_color = "lime"

    spawn_food()
    update_score()
    move()

def game_over():
    global game_running

    game_running = False
    winsound.Beep(400,300)

    text_pen.clear()
    text_pen.goto(0, 0)
    text_pen.write("GAME OVER\nPress R to Restart",
                   align="center", font=("Arial", 16, "bold"))

def toggle_pause():
    global paused

    if not game_running:
        return

    paused = not paused

    if paused:
        text_pen.goto(0,0)
        text_pen.write("PAUSED", align="center", font=("Arial", 16, "bold"))
    else:
        text_pen.clear()
        move()

def move():
    global score, high_score, d, level, snake_color

    if paused or not game_running:
        return

    head = saap[-1].copy()
    head[0] += offsets[kata][0]
    head[1] += offsets[kata][1]

    # self collision
    if head in saap:
        game_over()
        return

    # wall collision (FIXED)
    if head[0] < min_x or head[0] > max_x or head[1] < min_y or head[1] > max_y:
        game_over()
        return

    saap.append(head)

    # food eat
    if dist(head, khanaT) < 15:
        winsound.Beep(1000,100)
        score += 10

        # color change
        snake_color = food_color

        # level system
        level = score // 50 + 1

        # speed increase
        if d > 40:
            d -= level

        if score > high_score:
            high_score = score

        spawn_food()
        update_score()
    else:
        saap.pop(0)

    # draw snake
    pen.clearstamps()
    for i, s in enumerate(saap):
        pen.goto(s[0], s[1])

        if i == len(saap)-1:
            pen.color("yellow")
        else:
            pen.color(snake_color)

        pen.stamp()

    screen.update()
    turtle.ontimer(move, d)

# controls
def up():
    global kata
    if kata != "down":
        kata = "up"

def down():
    global kata
    if kata != "up":
        kata = "down"

def left():
    global kata
    if kata != "right":
        kata = "left"

def right():
    global kata
    if kata != "left":
        kata = "right"

# key bindings
screen.listen()
screen.onkey(up,"Up")
screen.onkey(down,"Down")
screen.onkey(left,"Left")
screen.onkey(right,"Right")
screen.onkey(toggle_pause,"space")
screen.onkey(reset_game,"r")
screen.onkey(reset_game, "R")

# start
draw_border()
reset_game()

turtle.done()
