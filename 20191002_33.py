import turtle as ts

def turn_right() :
    ts.setheading(0)
    ts.forward(10)
    
def turn_up() :
    ts.setheading(90)
    ts.forward(10)

def turn_left() :
    ts.setheading(180)
    ts.forward(10)

def turn_down() :
    ts.setheading(270)
    ts.forward(10)

def blank() :
    ts.clear()

ts.shape ("turtle")
ts.speed (0)
ts.onkeypress(turn_right, "Right")
ts.onkeypress(turn_up, "Up")
ts.onkeypress(turn_left, "Left")
ts.onkeypress(turn_down, "Down")
ts.onkeypress(blank, "Escape")
ts.listen()
