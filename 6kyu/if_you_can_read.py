#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# Kata from https://www.codewars.com/kata/if-you-can-read-this-dot-dot-dot/discuss/python
# Fun little one to convert a message into the NATO Phonic Alphabet
def to_nato(s):
    phonic_alpha = { "a" : "Alfa", "b" : "Bravo", "c" : "Charlie", "d" : "Delta",
    "e" : "Echo", "f" : "Foxtrot", "g" : "Golf", "h" : "Hotel", "i" : "India",
    "j" : "Juliett", "k" : "Kilo", "l" : "Lima", "m" : "Mike", "n" : "November",
    "o" : "Oscar", "p" : "Papa", "q" : "Quebec", "r" : "Romeo", "s" : "Sierra",
    "t" : "Tango", "u" : "Uniform", "v" : "Victor", "w" : "Whiskey",
    "x" : "Xray", "y" : "Yankee", "z" : "Zulu" }
    out = ""
    for c in s:
        if c.lower().isalpha():
            out = out + " " + phonic_alpha[c.lower()]
        if c in ".?!,":
            out = out + c
    return out
