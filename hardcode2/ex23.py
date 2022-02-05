import sys  # far as i know i'm still only using argv from sys, as sys.argv
script, encoding, error = sys.argv  # encoding still opaque, as is error


def main(language_file, encoding, errors):
    line = language_file.readline()  # okay,

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()  # all strip() does is remove \n from the line.
    raw_bytes = next_lang.encode(encoding, errors=errors)  # turn str to bytes
    cooked_string = raw_bytes.decode(encoding, errors=errors)  # and back

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)

"""This script is to acquaint one with strings n shit."""


"""Small history lesson in encoding, ASCII is 8-bit encoding, only works for
English because of 256 possibilities - each letter gets a binary number between
0 and 255 so 00000000 - 11111111.  Unicode was the world's solution and is 
32-bit but thats 4 billion characters and there is a lot of wasted space.  The
smart solution is to encode most shit in 8-bit and then jump out to higher
orders (16- or 32-bit) where needed.  UTF-8, Universal Transformation Format.

b'\xe6\x96\x87\xe8\xa8\x80'

here's a string of raw bytes for example (the b is for bytes).  what table of
characters do you want to use to decode this string of bytes?  how's about the
UTF-8 table?  

raw_bytes = b'\xe6\x96\x87\xe8\xa8\x80'
now...
raw_bytes.decode()
boom - 文言
it decoded the byte string using the UTF-8 table
just like 
'文言'.encode() gives you...
b'\xe6\x96\x87\xe8\xa8\x80'

"""