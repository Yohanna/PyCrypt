from colorama import init, Fore, Back, Style
import string
from PyErrors import TypeError

# init() # Need to be enabled when running on cmd


def caeser(message, key, mode='encrypt'):
    """
    Caesar cipher, A simple substitution cipher of type
    monoalphabetic substitution (using same key through out
    the encryption )

    :param message: Text to be encrypted/decrypted
    :param key: Key used to encryption/decryption
    :param mode: e: Encrypt the text, d: decrypt the text
    :return: Cipher/Plain Text (according to the mode)
    """

    # every possible symbol that can be encrypted
    SYMBOLS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

    # stores the encrypted/decrypted form of the message
    translated = ''

    # run the encryption/decryption code on each symbol in the message string
    for symbol in message:
        if symbol in SYMBOLS:
            # get the encrypted (or decrypted) number for this symbol
            num = SYMBOLS.find(symbol)  # If symbol is lowercase

            if mode == 'encrypt':
                num = (num + key) % len(SYMBOLS)
            elif mode == 'decrypt':
                num = (num - key) % len(SYMBOLS)
            else:
                raise TypeError(mode, "Types allowed are: encrypt or decrypt")

            # add encrypted/decrypted number's symbol at the end of translated
            translated += SYMBOLS[num]

        else:
            # just add the symbol without encrypting/decrypting
            translated += symbol

    return translated


def rot13(message, mode='encrypt'):
    return caeser(message, 13, mode)


def reverse(text):
    return text[::-1]  # Extended Slices


print(caeser('This Is my Secret message. 23421 @ // \\', 12))
