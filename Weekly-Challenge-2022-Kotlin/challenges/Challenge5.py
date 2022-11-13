"""
/*
 * Reto #5
 * ASPECT RATIO DE UNA IMAGEN
 * Fecha publicación enunciado: 01/02/22
 * Fecha publicación resolución: 07/02/22
 * Dificultad: DIFÍCIL
 *
 * Enunciado: Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
 * - Nota: Esta prueba no se puede resolver con el playground online de Kotlin. Se necesita Android Studio.
 * - Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */
"""

import requests
from PIL import ImageFile

TEST_URL = 'https://cdn.wallpapersafari.com/31/78/t57emR.jpg'


def get_final_ratio(width: 'int', height: 'int'):
    if height > width:
        raise Exception(
            f"Height: {height} can't be greater than width: {width}")
    denominator = 2
    while denominator < width:
        if width % denominator == 0 and height % denominator == 0:
            width = int(width / denominator)
            height = int(height / denominator)
            denominator = 1
        denominator = denominator + 1

    return f'Final ratio is: {int(width)}:{int(height)}'


def get_aspect_ratio(url):
    image_content = requests.get(url).content

    parser = ImageFile.Parser()
    parser.feed(image_content)

    if parser.image:
        (width, height) = parser.image.size
        if height > width:
            width, height = height, width
        return get_final_ratio(width, height)


def main():
    print(get_aspect_ratio(TEST_URL))


if __name__ == '__main__':
    main()
