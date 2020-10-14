import turtle as tp

def blink () :
    tp.clear()

tp.penup()
tp.goto (-300, 300)
tp.pendown()
tp.shape("turtle")
tp.speed (0)
tp.pensize (3)
#tp.hideturtle ()
tp.onscreenclick (tp.goto)
tp.onkeypress(blink, "Escape")
tp.listen()
