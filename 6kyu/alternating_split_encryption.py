#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# Kata from https://www.codewars.com/kata/simple-encryption-number-1-alternating-split
# Works pretty nice as long as it is single lines of text. Multi-lines get kinda funky.
from math import floor
def decrypt(encrypted_text, n):
    if n < 1:
        return encrypted_text
    split = floor(len(encrypted_text)/2)
    tempUnchanged, tempChanged, out = encrypted_text[0:split], encrypted_text[split:], ""
    for index, c in enumerate(tempUnchanged):
        out = out + tempChanged[index] + c
    if len(tempChanged) > len(tempUnchanged):
        out = out + tempChanged[-1]
    return decrypt(out, n-1)

def encrypt(text, n):
    if n < 1:
        return (text)
    out, temp = "", ""
    for index, c in enumerate(text):
        if index % 2 == 0:
            temp += str(c)
        else:
            out += str(c)
    return encrypt(out+temp, n-1)
