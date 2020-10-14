import turtle as t

def spiral(length) :
      if length <= 5 :
            return
      t.forward(length)
      t.right(90)
      spiral(length-5)

t.speed(5)
spiral(200)
