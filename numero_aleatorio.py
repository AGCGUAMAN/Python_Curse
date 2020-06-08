#-*- coding: utf-8 -*-
import random

def run():
    number_found = False
    random_number = random.randint(0, 100)

    while not number_found:
        number = int(input('Intenta un número que se encuentre entre 0 y 100: '))


        if number == random_number:
            print('Felicidades ¡Encontraste el Numero!')
            number_found = True
        elif number > random_number:
            print('El número es más pequeño!!!')
        else:
            print('El número es más grande!!!')
          


if __name__ == '__main__':
    run()