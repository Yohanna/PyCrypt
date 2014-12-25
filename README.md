[![Build Status](https://travis-ci.org/Yohanna/PyCrypt.svg?branch=master)](https://travis-ci.org/Yohanna/PyCrypt)
[![Analytics](https://ga-beacon.appspot.com/UA-57898843-1/PyCrypt/README.md)](https://github.com/igrigorik/ga-beacon)
[![License](https://img.shields.io/badge/license-Affero%20GPL-blue.svg?style=flat)](https://github.com/Yohanna/PyCrypt/blob/master/LICENSE)



PyCrypt
=======

PyCrypt is a (work in progress) python module implementing some basic cryptographic algorithms.

The purpose of the module is to serve as an introduction to the field of cryptography starting from some common and trivial algorithms up to [Public Key Cryptography](http://en.wikipedia.org/wiki/Public-key_cryptography) and Textbook [RSA](http://en.wikipedia.org/wiki/RSA_(cryptosystem)).

Also, some [Cryptanalysis](http://en.wikipedia.org/wiki/Cryptanalysis) will be tackled along the way. Specifically [Frequency Analysis](http://en.wikipedia.org/wiki/Frequency_analysis) against simple substitution ciphers.


### Implemented:

* Reverse Cipher ( Not sure I can even call it a cipher! )
* [Caeser Cipher](http://en.wikipedia.org/wiki/Caesar_cipher)
* [ROT13](http://en.wikipedia.org/wiki/ROT13)
* [Transposition cipher](http://en.wikipedia.org/wiki/Transposition_cipher)

### TODO

* [Vigenère cipher](http://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)
    * [Beaufort cipher](http://en.wikipedia.org/wiki/Beaufort_cipher)
* [Affine cipher](http://en.wikipedia.org/wiki/Affine_cipher)
* [Multiplicative Ciphers](http://www.nku.edu/~christensen/section%206%20multiplicative%20ciphers.pdf) (PDF)
* [Playfair cipher](http://en.wikipedia.org/wiki/Playfair_cipher)
* [One-time pad](http://en.wikipedia.org/wiki/One-time_pad)
* [Running key cipher](http://en.wikipedia.org/wiki/Running_key_cipher)

### Development

The master branch contains the latest stable codebase.

The [dev](https://github.com/Yohanna/PyCrypt/tree/dev) branch contains new features/algorithms to the module, which will be merged into master when it passes the build.

======

Some of the algorithms here will be based upon or an edited version of [Hacking Secret Ciphers with Python](http://inventwithpython.com/hacking) (BSD Licensed)
