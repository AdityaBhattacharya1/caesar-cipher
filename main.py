import string

# Encrypted = (x + n) % 26
# x = original alphabet, n = shift, 26 refers to the total number of alphabets in the english lexicon


def caesar(text, shift, alphabets):
    # Transposes alphabets. (alphabet + shift)
    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]

    # Mapping the shifted alphabets and the original alphabets
    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabets = ''.join(shifted_alphabets)

    # Making a table of the final alphabet and the final shifted alphabet (piled on top of each other)
    table = str.maketrans(final_alphabet, final_shifted_alphabets)

    # Translate the text, referring to the translation table made before.
    return text.translate(table)


# Test text encryption.
plain_text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(caesar(plain_text, 7, [string.ascii_lowercase,
                             string.ascii_uppercase, string.punctuation]))


# Alternate method of encryption
# def encrypt(text, shift):
#     result = ""

#     # traverse text
#     for i in range(len(text)):
#         char = text[i]

#         # Encrypt uppercase characters
#         if (char.isupper()):
#             result += chr((ord(char) + shift-65) % 26 + 65)

#         # Encrypt lowercase characters
#         else:
#             result += chr((ord(char) + shift - 97) % 26 + 97)

#     return result


# # check the above function
# text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# shift = 7
# print "Text  : " + text
# print "Shift : " + str(shift)
# print "Cipher: " + encrypt(text, shift)
