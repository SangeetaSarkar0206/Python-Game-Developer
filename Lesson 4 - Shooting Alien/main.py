import pgzrun
from random import randint

# window title
TITLE = "Shoot The Alien"
WIDTH = 400
HEIGHT = 400

# message
msg = ""

# add sprites
alien = Actor ("alien")
# alien.pos = 100,100


def draw () :
    screen.clear ()
    screen.fill ("#8bc6e8")
    alien.draw ()    # to draw the alien
    screen.draw.text (msg, center = (WIDTH/2, 100))

def place_alien () :
    alien.x = randint (50, WIDTH-50)
    alien.y = randint (50, WIDTH-50)

def on_mouse_down (pos) :
    global msg
    if alien.collidepoint (pos) :
        msg = "Good Shot"
        sounds.eep.play ()
        place_alien ()
    else :
        msg = "Shot Missed"

place_alien ()
pgzrun.go ()