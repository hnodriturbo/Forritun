#Hreiðar Pétursson
#31 janúar 2023
#Turtle verkefni

import turtle
"""
fred=turtle
fred.shape("turtle")
fred.color("red")
for i in range(4):
    for x in range(4):
        fred.forward(100)
        fred.left(90)
    fred.up()
    fred.forward(120)
    fred.down()
"""
"""
fred = turtle
fred.shape("turtle")
fred.color("red")
fred.width(10)
for x in range(20):

    fred.forward(100)
    fred.up()
    fred.right(90)
    fred.forward(20)
    fred.right(90)
    fred.down()
    fred.forward(100)

    fred.up()
    fred.left(90)
    fred.forward(20)
    fred.left(90)
    fred.down()
"""


"""
fred = turtle
fred.shape("turtle")
fred.color("red")
fred.width("5")

lengd = 10

for x in range(10):

    fred.forward(lengd)
    fred.up()
    fred.right(90)
    fred.forward(5)
    fred.right(90)
    fred.forward(lengd)
    fred.left(90)
    fred.forward(5)
    fred.left(90)
    fred.down()

    lengd = lengd + 20

fred.done()
"""
"""
fred = turtle
fred.shape("turtle")
fred.color("blue")
fred.width("2")

radius = 10

for x in range(10):
    fred.circle(radius)
    radius = radius + 10

fred.done()


"""
"""
fred = turtle
fred.shape("turtle")
fred.color("blue")
fred.width("2")

radius = 10
for x in range(15):
    fred.circle(radius)

    radius = radius + 10
    fred.up()
    fred.right(90)
    fred.forward(10)
    fred.left(90)
    fred.down()
"""

fred = turtle
fred.shape("turtle")
fred.color("blue")
fred.width("2")

breyta1 = 2
breyta2 = 5
for x in range(100):

    fred.forward(breyta1)
    fred.left(120)
    fred.forward(breyta2)
    fred.color("green")
    breyta1 = breyta1 + 2
    breyta2 = breyta2 + 2

fred.done()
