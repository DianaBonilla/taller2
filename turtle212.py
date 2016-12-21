## Diana Bonilla
import turtle
t = turtle.Pen()
##t.forward(50)
##t.left(90)
##t.forward(50)
##t.left(90)
##t.forward(50)
##t.left(90)
##t.forward(50)
##turtle.getscreen()._root.mainloop()

## estrella
##t.reset()
##for x in range(1,9):
##    t.forward(300)
##    t.left(225)

##ESTRELLA CON PUNTAS N
t.reset()
n = int(input("Ingrese un numero impar: "))
an = 180/n
an2= 180-an

t.reset()
for x in range(n):
    t.forward(100)
    t.left(an2)

##CUADRADO
##def micuadrado(size):
##    for x in range(1,5):
##        t.forward(size)
##        t.left(90)
##
##micuadrado(100)
