"""
 * Reto #4
 * ÁREA DE UN POLÍGONO
 * Fecha publicación enunciado: 24/01/22
 * Fecha publicación resolución: 31/01/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
"""


class Rectangle:
    def __init__(self, width: 'float', height: 'float') -> None:
        self.width = width
        self.height = height

    def calc_area(self):
        return self.width * self.height


class Triangle:
    def __init__(self, base: 'float', height: 'float') -> None:
        self.base = base
        self.height = height

    def calc_area(self):
        return (self.base * self.height) / 2


class Square:
    def __init__(self, side: 'float') -> None:
        self.side = side

    def calc_area(self):
        return self.side ** 2


def area(polygon: 'Square | Triangle | Rectangle'):
    return polygon.calc_area()


def main():
    print(area(Square(5)))
    print(area(Triangle(4, 2)))
    print(area(Rectangle(8, 2)))


if __name__ == '__main__':
    main()
