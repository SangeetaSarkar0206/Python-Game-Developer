import pgzrun

# screen size
WIDTH = 800
HEIGHT = 600

def draw () :
    screen.fill ("#a2e8c2")
    # draw RECTANGLE (rect, color), rect : (x,y), (w,h)
    r1 = Rect ((40,40), (100,50))
    r2 = Rect ((40,100), (100,50))
    screen.draw.rect (r1, "black")
    screen.draw.filled_rect (r2, "red")

    # draw CIRCLE (start-pos, radius, color)
    screen.draw.circle ((200,50),40, "black")
    screen.draw.filled_circle ((200,150),40, "black")

    # draw LINE (start-pos, end-pos, color)
    screen.draw.line ((250,50), (250, 300), "red")

    # draw TEXT (gcolor = "gradient color", owidth = "outline width" https://pygame-zero.readthedocs.io/en/stable/ptext.html)
    screen.draw.text ("Text is here", (450,100), fontsize = 48,color = "black", gcolor = "yellow", owidth = 2, ocolor = "white")
pgzrun.go ()