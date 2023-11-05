import turtle

t= turtle.Turtle()
t.screen.bgcolor("#e0def5")
t.pensize(2)
t.color("#0c2419")
t.left(90)
t.backward(100)
t.speed(200)
t.shape("turtle")

def tree(i) :
 if i<10 :
   return
 else:
   t.forward(i)
   t.color("#7070c2")
   t.circle(2)
   t.color("#2f4439")
   t.left(30)
   tree(3*i/4)
   t.right(60)
   tree(3*i/4)
   t.left(30)
   t.backward(i)
tree(100)
turtle.done()