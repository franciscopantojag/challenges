"""
/*
 * Reto #10
 * EXPRESIONES EQUILIBRADAS
 * Fecha publicación enunciado: 07/03/22
 * Fecha publicación resolución: 14/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */
"""
from utils.verify_type import verify_type


def is_balanced(expression: 'str'):
    verify_type(str, expression)
    dictionary = {
        "{": "}",
        "(": ")",
        "[": "]",

    }
    for index, char in enumerate(expression):
        value = dictionary.get(char)
        if value:
            try:
                index_test = expression.index(char)
                index_test2 = expression.index(value, index_test)
            except:
                return False
            index_test = expression.index(char)
            if index_test <= len(expression) - 1:
                expression = expression[:index_test] + \
                    expression[(index_test+1):]
            else:
                expression = expression[:index_test]
            index_test2 = expression.index(value, index_test)
            if index_test2 <= len(expression) - 1:
                expression = expression[:index_test2] + \
                    expression[(index_test2+1):]
            else:
                expression = expression[:index_test2]
    all_chars = list(dictionary.keys()) + list(dictionary.values())
    for char in expression:
        if char in all_chars:
            return False
    return True


TEST_STR = "{a + b [c] * (2x2)}}}}"
TEST_STR1 = "{ [ a * ( c + d ) ] - 5 }"
TEST_STR2 = "{ a * ( c + d ) ] - 5 }"
TEST_STR3 = "{a^4 + (((ax4)}"
TEST_STR4 = " a * ( c + d ) + ( 2 - 3 )[ - 5] }"
TEST_STR5 = "{{{{{{}}}}}}"
print(is_balanced(TEST_STR))
print(is_balanced(TEST_STR1))
print(is_balanced(TEST_STR2))
print(is_balanced(TEST_STR3))
print(is_balanced(TEST_STR4))
print(is_balanced(TEST_STR5))
