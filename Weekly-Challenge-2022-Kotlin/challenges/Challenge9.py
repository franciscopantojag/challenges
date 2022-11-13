"""
/*
 * Reto #9
 * CÓDIGO MORSE
 * Fecha publicación enunciado: 02/03/22
 * Fecha publicación resolución: 07/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */
"""

from utils.verify_type import verify_type
from utils.reverse_dic import reverse_dic


LANG_CHAR_TO_MORSE = {
    'A': '.-',     'B': '-...',   'C': '-.-.',
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'Ñ': '-.-',
    'O': '---',    'P': '.--.',   'Q': '--.-',
    'R': '.-.',    'S': '...',    'T': '-',
    'U': '..-',    'V': '...-',   'W': '.--',
    'X': '-..-',   'Y': '-.--',   'Z': '--..',

    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',

    '"': ".-..-.", '.': ".-.-.-", ',': '-..-',
    '?': '..-..', '/': '-..-.', ' ': ''
}

MORSE_CHAR_TO_LANG = reverse_dic(LANG_CHAR_TO_MORSE)


def is_morse(string: 'str'):
    morse_chars = {'', ' ', '.', '-'}
    return all([char in morse_chars for char in string])


def encode_lang_char(lang_char: 'str'):
    upper_char = lang_char.upper()
    from_dic = LANG_CHAR_TO_MORSE.get(upper_char)
    return from_dic if isinstance(from_dic, str) else '.'


def encode_morse(paragraph: 'str'):
    return ' '.join([encode_lang_char(char) for char in paragraph])


def decode_morse_char(morse_char: 'str'):
    from_dic = MORSE_CHAR_TO_LANG.get(morse_char)
    return from_dic if isinstance(from_dic, str) else ''


def decode_morse_word(morse_word: 'str'):
    morse_chars = morse_word.split(' ')
    return ''.join([decode_morse_char(morse_char) for morse_char in morse_chars])


def decode_morse(paragraph: 'str'):
    morse_words = paragraph.split('  ')
    return ' '.join([decode_morse_word(morse_word) for morse_word in morse_words])


def decoder(paragraph: 'str'):
    verify_type(str, paragraph)
    result = decode_morse(paragraph) if is_morse(
        paragraph) else encode_morse(paragraph)
    print(result)
    return result


str_test = 'Chocapic. Es una marca de cereales?'
decoder(str_test)
decoder(decoder(str_test))
