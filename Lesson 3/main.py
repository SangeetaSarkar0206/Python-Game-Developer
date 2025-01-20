import pgzrun
import random

WIDTH = 600
HEIGHT = 400


def draw () :
    screen.fill ("black")

    w = 500
    h = 100
    for x in range (10) :
        r1 = Rect ((0,0), (w,h))
        r1.center = (WIDTH/2, HEIGHT/2)       # align from center of screen
        screen.draw.rect (r1, (random.randint (0,255), random.randint (0,255), random.randint (0,255)))
        w -= 20
        h +=20


pgzrun.go ()