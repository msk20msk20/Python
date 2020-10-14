import turtle as t

def tree (length) :
      if length <= 5 :
            return
      new_len = length * 0.7
      t.forward(length)
      t.right(20)
      tree(new_len)
      t.left(40)
      tree(new_len)
      t.right(20)
      t.backward(length)


t.speed(0)
t.left(90)
tree(70)
