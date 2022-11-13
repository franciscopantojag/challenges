"""
/*
 * Reto #7
 * CONTANDO PALABRAS
 * Fecha publicación enunciado: 14/02/22
 * Fecha publicación resolución: 21/02/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
"""


def count_words(string: 'str'):
    if not isinstance(string, str):
        raise Exception(f'Invalid string: {string}')
    result = {}
    current_word = ''
    for char in string:
        if char.isalpha():
            current_word += char
        else:
            if len(current_word) > 0:
                low_word = current_word.lower()
                from_dic = result.get(low_word)
                current_count_word = from_dic if isinstance(
                    from_dic, int) else 0
                result[low_word] = current_count_word + 1
                current_word = ''
    for key, value in result.items():
        print(f'{key} se ha repetido {value} {"vez" if value == 1 else "veces"}')
    return result


count_words(
    'Hola, mi nombre es brais. Mi nombre completo es Brais Moure (MoureDev).')
