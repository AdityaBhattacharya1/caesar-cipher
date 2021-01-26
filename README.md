# Introduction

A simple Caesar Cipher encryptor.

# How a Caesar Cipher works

The basic formulae on which the Cipher works are:

### Encryption (Ex) = (x + n) % 26

### Decryption (Dx) = (x - n) % 26

<br>
Where x = original alphabet, n = shift, 26 refers to the total number of alphabets in the English lexicon. 
<br><br>
<img src="https://media.geeksforgeeks.org/wp-content/uploads/ceaserCipher.png" align="center">
<br><br>

*For example, the alphabets shifted to 7:* <br>
**Original**: ABCDEFGHIJKLMNOPQRSTUVWXYZ <br>
**Encrypted**: HIJKLMNOPQRSTUVWXYZABCDEFG <br>
**Shift**: 7 <br>

# DS&A used for the alternate method

The alternate method for encryption uses the chr() and ord() functions.

## chr() function

The chr() method accepts a number representing the Unicode of a character and returns the actual character corresponding to the numeric code.

## ord() function

The ord() method is used to convert a character to its numeric representation in Unicode. It accepts a single character and returns the number representing its Unicode.

# Clone project

`git clone https://github.com/AdityaBhattacharya1/caesar-cipher/` <br>

`cd` into the directory <br>

`pip install -r requirements.txt` <br>

`python main.py`
