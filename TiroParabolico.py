from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def inside(xy):
    "Return True if xy within screen."
    "For making the game never end we only change "and" for "or" "
    return -200 < xy.x < 200 or -200 < xy.y < 200 

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'red')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'black')

    update()

def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 1.5

    if inside(ball):
        "for increasing speed we decrease the number of speed.y by decimals and we also"
        "add a speed. x, this speed.x will increase the speed also and make it faster"
        speed.y -= .20
        speed.x -= .10
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()