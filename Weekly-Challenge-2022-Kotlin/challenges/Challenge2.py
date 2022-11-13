"""
 * Reto #2
 * LA SUCESIÓN DE FIBONACCI
 * Fecha publicación enunciado: 10/01/22
 * Fecha publicación resolución: 17/01/22
 * Dificultad: DIFÍCIL
 *
 * Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
 * La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
 * 0, 1, 1, 2, 3, 5, 8, 13...
"""


def main():
    prev_fib = 0
    last_fib = 1
    for _ in range(0, 50):
        print(prev_fib)
        next_fib = prev_fib + last_fib
        prev_fib, last_fib = last_fib, next_fib


if __name__ == '__main__':
    main()
