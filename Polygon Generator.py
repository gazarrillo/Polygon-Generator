from turtle import *
from random import randint

wrong_value = True

while wrong_value:
    try:
        sides = int(input('Enter the number of sides, less than 3 to exit: '))
        wrong_value = False
    except ValueError:
        print('What you entered is not an interger, please try again.')

def makePolygon (sides, length, borderColor, width, fillColor):
    shape('turtle')
    pensize(width)
    pencolor(borderColor)
    fillcolor(fillColor)
    begin_fill()
    for i in range(sides):
        forward(length)
        left(angle)
    end_fill()

while sides >= 3:

    length = 600/sides

    angle = 360/sides

    width = (sides%20) + 1

    colors = ['coral', 'gold', 'brown', 'red', 'green', 'blue', 'yellow',
                  'purple', 'orange', 'cyan', 'pink', 'magenta', 'goldenrod']

    borderColor = colors[randint(0, 12)]
    fillColor = colors[randint(0, 12)]

    makePolygon(sides, length, borderColor, width, fillColor)

    wrong_value = True

    while wrong_value:
        try:
            sides = int(input('Enter the number of sides, less than 3 to exit: '))
            wrong_value = False
        except ValueError:
            print('What you entered is not an interger, please try again.')

    clear()
else:
    print('Thanks for using the polygon generator program')
