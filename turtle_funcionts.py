#-*- coding: utf-8 -*-

import turtle


def main():
    window = turtle.Screen()
    Alex = turtle.Turtle()

    make_square(Alex)

    turtle.mainloop()


def make_square(Alex):
    length = int(input('Tamaño de cuadrado: '))

    for i in range(4):
        make_line_and_turn(Alex, length)


def make_line_and_turn(Alex, length):
    Alex.forward(length)
    Alex.left(90)


if __name__ == '__main__':
    main()