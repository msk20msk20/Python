import turtle as t
import random
t.shape ("turtle")

def turn_up() :
    t.left (2)

def turn_down() :
    t.right (2)

def fire() :
    ang = t.heading()
    while t.ycor() > 0 :
        t.forward (15)
        t.right (5)
    d = t.distance (target, 0)
    t.sety(random.randint(10, 100))

    if d < 25 :
        t.color ("blue")
        t.write ("good!", False, "center", ("", 15))
    else :
        t.color ("red")
        t.write ("bad!", False, "center", ("", 15))
    t.color ("black")
    t.goto (-200, 10)
    t.setheading(ang)


#땅을 그립니다.
t.goto (-300, 0)
t.down()
t.goto (300, 0)

#목표 지점 그리기
target = random.randint (0, 250)
t.pensize (3)
t.color ("red")
t.up()
t.goto (target - 25, 2)
t.down()
t.goto (target + 25, 2)

#거북이 위치 지정하기
t.color ("black")
t.up()
t.goto (-200, 10)
t.setheading (20)


#거북이 이동 설정
t.onkeypress (turn_up, "Up")
t.onkeypress (turn_down, "Down")
t.onkeypress (fire, "space")

t.listen()
