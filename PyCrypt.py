from colorama import init, Fore, Back, Style
import string
from PyErrors import TypeError

# init() # Need to be enabled when running on cmd


def caeser(message, key, mode='encrypt', scope='all'):
    """
    Caesar cipher, A simple substitution cipher classed as a type of
    monoalphabetic substitution (using same key/replacements through out
    the encryption )

    :rtype : string
    :param message: Text to be encrypted/decrypted
    :param key: Key used to encryption/decryption
    :param mode: e: Encrypt the text, d: decrypt the text
    :return: Cipher/Plain Text (according to the mode)
    """

    # Every possible symbol that can be encrypted
    if scope is 'numbers' or scope is 'digits':  # Only digits will be encrypted
        symbols_list = string.digits
    elif scope is 'letters':
        symbols_list = string.ascii_letters
    elif scope is 'alphanumeric' or scope is 'alphanum':
        symbols_list = string.ascii_letters + string.digits
    elif scope is 'all':
        symbols_list = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    elif scope.isprintable():  # The user supplied a custom list
        symbols_list = scope
    else:
        raise TypeError(scope, 'Only list of strings are allowed!')

    # Stores the encrypted/decrypted form of the message
    translated = ''

    # run the encryption/decryption code on each symbol in the message string
    for symbol in message:
        if symbol in symbols_list:
            # get the encrypted (or decrypted) number for this symbol
            num = symbols_list.find(symbol)  # If symbol is lowercase

            if mode == 'encrypt':
                num = (num + key) % len(symbols_list)
            elif mode == 'decrypt':
                num = (num - key) % len(symbols_list)
            else:
                raise TypeError(mode, "Types allowed are: encrypt or decrypt")

            # add encrypted/decrypted number's symbol at the end of translated
            translated += symbols_list[num]

        else:
            # just add the symbol without encrypting/decrypting
            translated += symbol

    return translated


def rot13(message, mode='encrypt'):
    return caeser(message, 13, mode)


def reverse(text):
    return text[::-1]  # Extended Slices

