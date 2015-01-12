import string
import PyErrors
import math


def caeser(message, key, mode='encrypt', scope='all', custom=''):
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

    if scope is 'custom' and custom == '':
        raise PyErrors.SymbolsError("You need to provide a custom symbols list if you used the 'custom' option for scope")


    # Every possible symbol that can be encrypted
    if scope is 'numbers' or scope is 'digits':  # Only digits will be encrypted
        symbols_list = string.digits
    elif scope is 'letters':
        symbols_list = string.ascii_letters
    elif scope is 'alphanumeric' or scope is 'alphanum':
        symbols_list = string.ascii_letters + string.digits
    elif scope is 'all':
        symbols_list = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    elif scope is 'custom' and scope.isprintable():  # The user supplied a custom list
        symbols_list = custom
    else:
        raise PyErrors.TypeError(scope, "digits, letters, alphanumeric and all (printable characters), are the only allowed scope")

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
                raise PyErrors.TypeError(mode, "Types allowed are: encrypt or decrypt")

            # add encrypted/decrypted number's symbol at the end of translated
            translated += symbols_list[num]

        else:
            # just add the symbol without encrypting/decrypting
            translated += symbol

    return translated


def rot13(message, mode='encrypt', scope='all', custom=''):
    return caeser(message, 13, mode, scope, custom)


def reverse(text):
    return text[::-1]  # Extended Slices


class Transposition:
    @staticmethod
    def encrypt(message, key):

        if key > len(message) / 2:
            raise PyErrors.WeakKeyError("The key used '%s' can't be larger than half the message length '%s'." % (key, int(len(message)/2)))

        # Each string in cipher_text represents a column in the grid.
        # The number of columns in the grid equals to the key.
        columns = key

        cipher_text = [''] * columns

        # Loop through each column in cipher_text.
        for col in range(columns):
            pointer = col

            # Keep looping until pointer goes past the length of the message.
            while pointer < len(message):
                # Place the character at pointer in message at the end of the
                # current column in the cipher_text list.
                cipher_text[col] += message[pointer]

                # move pointer to point to next character in the message.
                pointer += columns

        # Convert the cipher_text list into a single string value and return it.
        return ''.join(cipher_text)

    @staticmethod
    def decrypt(message, key):

        # The transposition decrypt function will simulate the "columns" and
        # "rows" of the grid that the plain_text is written on by using a list
        # of strings.

        # The number of columns and rows in our transposition grid:
        columns = math.ceil(len(message) / key)
        rows = key
        # The number of "shaded boxes" in the last "column" of the grid:
        shaded_boxes = (columns * rows) - len(message)

        # Each string in plain_text represents a column in the grid.
        plain_text = [''] * columns

        # The col and row variables point to where in the grid the next
        # character in the encrypted message will go.
        col = 0
        row = 0

        for symbol in message:
            plain_text[col] += symbol
            col += 1  # point to next column

            # If there are no more columns OR we're at a shaded box, go back to
            # the first column and the next row.
            if (col == columns) or (col == columns - 1 and row >= rows - shaded_boxes):
                col = 0
                row += 1

        return ''.join(plain_text)

