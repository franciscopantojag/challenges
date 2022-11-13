"""
 * Reto #3
 * ¿ES UN NÚMERO PRIMO?
 * Fecha publicación enunciado: 17/01/22
 * Fecha publicación resolución: 24/01/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
"""


def isPrime(num: 'int'):
    if num < 2:
        return False
    for div in range(2, num):
        if num % div == 0:
            return False
    return True


def main():
    for num in range(1, 100):
        if (isPrime(num)):
            print(num)


if __name__ == '__main__':
    main()
